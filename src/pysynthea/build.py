from pathlib import Path
import sqlalchemy as sa

from .consts import *
from .utils_setup import *


def setup_db(database=DB_PATH):
    """
    Set up the local Synthea database depending on the specified type
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