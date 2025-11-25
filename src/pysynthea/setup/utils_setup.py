import requests, io, zipfile
from pathlib import Path
import pandas as pd

"""
Utilities to download, extract, and import Synthea databases into a SQL database.

This module provides helper functions to:

    - Download the full 10K Synthea database ('get_10k_db') and save it to disk.
    - Download a smaller Synthea database ZIP file ('get_small_db') and extract its contents.
    - Read CSV files from a directory and create tables in a SQL database ('create_tables').

All functions use Python standard libraries (requests, io, zipfile, pandas, pathlib) and
are compatible with SQLAlchemy engines for database interaction.

Dependencies
------------
pandas
requests

Typical usage
-------------
from pathlib import Path
from sqlalchemy import create_engine

# Download and extract
get_10k_db(url="http://example.com/synthea_10k.db", 
    output_dir=Path("data"), 
    output_path=Path("data/synthea_10k.db"))

get_small_db(url="http://example.com/synthea_small.zip", 
    extract_to=Path("data/small_db"))

# Load CSVs into a database
engine = create_engine("sqlite:///synthea.db")
create_tables(dir=Path("data/small_db"), engine=engine)
"""


#10K DATABASE
def get_10k_db(url, output_dir, output_path):
    """
    Download the big Synthea database file from a given URL and save it to disk.

    Parameters
    ----------
    url: str
        The URL to download the database from.
    output_dir: pathlib.Path
        Directory where the database file will be stored. Will be created if it doesn't exist.
    output_path: pathlib.Path
        Full path including filename where the downloaded file will be saved.
    
    Raises
    ------
    requests.HTTPError
        If the HTTP request for the URL fails.
    IOError
        If writing to the output file fails.
    """

    output_dir.mkdir(exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)


# SMALL DATABASE
def get_small_db(url, extract_to):
    """
    Download a ZIP file from a URL and extract its contents into a local folder.

    Parameters
    ----------
    url: str
        The URL to download the database from.
    extract_to: pathlib.Path
        The directory where the ZIP contents will be extracted. It will be created if it doesn't exist.

    Raises
    ------
    requests.HTTPError
        If the HTTP request fails.
    zipfile.BadZipFile
        If the downloaded file is not a valid ZIP archive.
    IOError
        If writing to the extract directory fails.
    """

    response = requests.get(url)
    zip = io.BytesIO(response.content)
    with zipfile.ZipFile(zip, 'r') as z:
        z.extractall(extract_to)


def create_tables(dir, engine):
    """
    Read all CSV files in a directory and create tables in a SQLite database. Uses SQLAlchemy.
    Each CSV file will become a table with the same name as the file (without extension).
    Existing tables with the same name will be replaced.

    Parameters
    ----------
    dir: pathlib.Path or str
        Path to the directory containing CSV files.
    engine: sqlalchemy.engine.Engine
        SQLAlchemy engine connected to the target database.
    """
    
    for file in Path(dir).glob('*.csv'):
        table_name = file.stem
        df = pd.read_csv(file)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False, method="multi")
