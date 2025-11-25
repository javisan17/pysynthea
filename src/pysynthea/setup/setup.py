from pathlib import Path
import sqlalchemy as sa

from ..consts import *
from .utils_setup import *

"""
Synthea database setup and connection utilities.

This module provides functions to:

    - Download and prepare the full 10K Synthea database ('setup_db').
    - Download and extract the smaller Synthea database ('setup_db' with 'small').
    - Build database tables from CSV files for the small database ('create_tables').
    - Connect to a local DuckDB database using SQLAlchemy ('connect_db').

The functions handle downloading data from predefined URLs, creating required
directories, and building a SQL database ready for queries.

Dependencies
------------
utils_setup.py module 
consts.py module
sqlalchemy

Typical usage
-------------
from pathlib import Path
import sqlalchemy as sa
from pysynthea.setup.setup import setup_db, connect_db

# Prepare the small Synthea database
setup_db(database="small")

# Connect to the database
conn = connect_db(database="small")
result = conn.execute("SELECT * FROM patients LIMIT 5")
for row in result:
    print(row)
"""


def setup_db(database=DB_PATH):
    """
    Set up the local Synthea database depending on the specified type.

    Depending on the specified 'database' parameter, this function will:
    - Download the full 10K Synthea database if `database` equals `DB_PATH`.
    - Download and extract the small Synthea database if `database` equals "small".
    - Build the database tables from CSV files for the small database.

    Parameters
    ----------
    database: str or pathlib.Path, optional
        Path to the target database file or "small" to use the smaller Synthea dataset.
        Default is `DB_PATH`.
    
    Raises
    ------
    FileNotFoundError
        If the required directories or files cannot be created or accessed.
    requests.HTTPError
        If downloading the database from the URL fails.
    zipfile.BadZipFile
        If the small database ZIP is invalid.
    """

    if database == DB_PATH:
        if Path(database).exists():
            return
        
        #Bring and download the db
        get_10k_db(url=DB_URL, output_dir=DATA_DIR , output_path=DB_PATH)

    database = DB_SMALL_PATH if database == "small" else database
    if database == DB_SMALL_PATH:
        if Path(database).exists():
            return

        # Download data
        get_small_db(url=DB_SMALL_URL, extract_to=CSV_DIR)

        # Build db
        engine = sa.create_engine(f"duckdb:///{DB_SMALL_PATH}")

        with engine.connect() as conn:
            with conn.begin():
                # Create tables
                create_tables(dir=CSV_DIR, engine=conn)


def connect_db(database=DB_PATH):
    """
    Connect to a local DuckDB database.
    This function returns a connection to the specified DuckDB database file.
    If 'database' is "small", it connects to the small Synthea dataset.

    Parameters
    ----------
    database: str or pathlib.Path, optional
        Path to the target database file or "small" to use the smaller Synthea dataset.
        Default is `DB_PATH`.

    Returns
    -------
    sqlalchemy.engine.Connection
        A SQLAlchemy connection object connected to the specified DuckDB database.

    Raises
    ------
    FileNotFoundError
        If the specified database file does not exist.
    """

    database = DB_SMALL_PATH if database == "small" else database
    if not Path(database).exists():
        if database == DB_PATH:
            raise FileNotFoundError("Not found default db.")
        elif database == DB_SMALL_PATH:
            raise FileNotFoundError("Not found small db.")
        else:
            raise FileNotFoundError("Not found db. Incorrect path.")
    
    return sa.create_engine(f"duckdb:///{database}").connect()