"""
TEST de montar la base de datos en local desde repo de Zenodo
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from pysynthea.build.setup import setup_db, connect_db
import sqlalchemy as sa

def main():
    setup_db()


if __name__ == "__main__":
    main()