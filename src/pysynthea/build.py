from pathlib import Path
import sqlalchemy as sa

from .consts import *
from .utils import get_csv, create_tables


def setup_db():
    """
    Downloading csv files and building a local DuckDB  
    """

    if Path(DB_PATH).exists():
        return

    # Download data
    get_csv(url=ZIP_URL, extract_to=CSV_DIR)

    # Build db
    engine = sa.create_engine(f"duckdb:///{DB_PATH}")

    with engine.connect() as conn:
        with conn.begin():
            # Create tables
            create_tables(dir=CSV_DIR, engine=conn)


def connect_db():
    """
    Connect to a local DuckDB database.
    """

    if not Path(DB_PATH).exists():
        raise FileNotFoundError("Not found db. Run setup_db().")

    return sa.create_engine(f"duckdb:///{DB_PATH}").connect()