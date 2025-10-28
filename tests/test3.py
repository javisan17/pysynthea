
"""
TEST de pruebas 3. Comprobar que se pueden crear conceptsets adecuados
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from pysynthea.concept_set import *
from pysynthea.build import *

def main():
    # Connection to synthea_10000
    conn = connect_db()

    # Testing function
    df = get_concept_set(
        conn=conn,
        concept_ids=[1032443],          # DEBEN PASAR ARGUMENTOS COMO LISTAS
        concept_names=["Diabetes mellitus"],
        include_descendants=True
    )

    # Results
    print(df.head())
    print(df.columns)
    print(len(df))


    conn.close()


if __name__ == "__main__":
    main()