import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from pysynthea.build import setup_db, connect_db
import sqlalchemy as sa

def main():

    # Build db
    setup_db()
    
    # Connect db
    conn = connect_db()

    # Queries
    cur = conn.execute(sa.text("select  from PERSON"))
    count = cur.fetchone()
    print(count)

    conn.close()

if __name__ == "__main__":
    main()