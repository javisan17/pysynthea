"""
TEST de pruebas 1. Montar base de datos pequeña, consultas varias, cohortes... 
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from pysynthea.setup.setup import setup_db, connect_db
import sqlalchemy as sa

def main():

    # Build db
    setup_db()
    
    # Connect db
    conn = connect_db()

    # Queries
    cur = conn.execute(sa.text("""select count(*) from person;"""))

    cursor = cur.fetchone()
    print(cursor)

    conn.close()


if __name__ == "__main__":
    main()