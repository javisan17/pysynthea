"""
TEST 1. It verifies:
    - Small database setup using 'setup_db()'
    - Connection to said database by using 'connect_db()'
    - Data exists by executing a simple query on the 'person' table.
       Prints results for manual verification

Dependencies
-------------
sqlalchemy
setup.py

Notes
-----
- This is a simple integration test, not a unit test.
- Ensure that the database URLs and paths in `pysynthea.consts` are correct.
- Intended to run as a standalone script.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

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