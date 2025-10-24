from pathlib import Path

#Direct link to db file
DB_URL = ''
DB_SMALL_URL = 'https://github.com/OHDSI/EunomiaDatasets/raw/main/datasets/Synthea27Nj/Synthea27Nj_5.4.zip'


#RUTAS
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SRC_DIR = BASE_DIR / "src"
PYSYNTHEA = SRC_DIR / "pysynthea"
DATA_DIR = PYSYNTHEA / "data"
CSV_DIR = DATA_DIR / "csv"


DB_PATH = DATA_DIR /'synthea10k.duckdb'
DB_SMALL_PATH = DATA_DIR /'synthea_small.duckdb'
