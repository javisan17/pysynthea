from pathlib import Path
import sqlalchemy as sa

from .consts import *
from .utils import get_csv, create_tables


def setup_db():
    """
    Downloading csv files and building a local DuckDB  
    """

    if Path(DB_SMALL_PATH).exists():
        return

    # Download data
    get_csv(url=ZIP_URL, extract_to=CSV_DIR)

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