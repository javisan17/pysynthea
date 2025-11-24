"""
TEST 2. It verifies:
    - Local database set up from the Zenodo repository.
        Uses setup_db to download and setup the database.

Dependencies
------------
setup.py

Notes
-----
- This is an integration test, not a unit test.
- Requires internet access to download the database.
- Intended to run as a standalone script for manual verification.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from pysynthea.setup.setup import setup_db

def main():
    setup_db()


if __name__ == "__main__":
    main()