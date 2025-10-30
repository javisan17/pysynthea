import requests, io, zipfile
from pathlib import Path
import pandas as pd

#10K DATABASE
def get_10k_db(url, output_dir, output_path):
    """

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
    Download a ZIP file from a URL and extract its contents into a local folder
    """

    response = requests.get(url)
    zip = io.BytesIO(response.content)
    with zipfile.ZipFile(zip, 'r') as z:
        z.extractall(extract_to)


# def extract_csv(zip, extract_to):
#     """
#     Extract the content of a zip file into a local folder
#     """

#     with zipfile.ZipFile(zip, 'r') as z:
#         z.extractall(extract_to)

def create_tables(dir, engine):
    """
    Read all CSV files in a directory and create tables in a SQLite database.
    """
    
    for file in Path(dir).glob('*.csv'):
        table_name = file.stem
        df = pd.read_csv(file)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False, method="multi")
