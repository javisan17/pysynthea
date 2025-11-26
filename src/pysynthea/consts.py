from pathlib import Path

"""
Constants and file paths for the Synthea database setup.

This module defines:

- URLs for downloading the full CP and small Synthea datasets.
- Directory paths for storing source code, data, and CSV files.
- File paths for the DuckDB databases (full and small versions).

Typical usage
-------------
from pysynthea.consts import DB_SMALL_URL, DB_PATH, DB_SMALL_PATH
"""

# Direct links to db file:
# Direct link to the full CP Synthea database
DB_URL = 'https://zenodo.org/records/17722472/files/synthea_cp.duckdb?download=1'
# Direct link to the small Synthea database (ZIP file)
DB_SMALL_URL = 'https://github.com/OHDSI/EunomiaDatasets/raw/main/datasets/Synthea27Nj/Synthea27Nj_5.4.zip'


# Directory paths:
# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Source code directory
SRC_DIR = BASE_DIR / "src"
# Root directory of the pysynthea package
PYSYNTHEA = SRC_DIR / "pysynthea"
# Directory to store downloaded data
DATA_DIR = PYSYNTHEA / "data"
# Directory for CSV files extracted from ZIP
CSV_DIR = DATA_DIR / "csv"


# Database file paths:
# Full CP DuckDB database
DB_PATH = DATA_DIR /'synthea_cp.duckdb'
# Small DuckDB database
DB_SMALL_PATH = DATA_DIR /'synthea_small.duckdb'
