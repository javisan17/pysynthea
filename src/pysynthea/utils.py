import requests, io, zipfile
from pathlib import Path
import pandas as pd

def get_csv(url, extract_to):
    """
    Download a ZIP file from a URL and extract its contents into a local folder
    """

    response = requests.get(url)
    zip = io.BytesIO(response.content)
    with zipfile.ZipFile(zip, 'r') as z:
        z.extractall(extract_to)

def create_tables(dir, engine):
    """
    Read all CSV files in a directory and create tables in a SQLite database.
    """
    
    for file in Path(dir).glob('*.csv'):
        table_name = file.stem
        df = pd.read_csv(file)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False, method="multi")
