
"""
TEST for ConceptSet class. Making sure correct ConceptSets can be created 
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

from pysynthea.concept_set.concept_class import *
from pysynthea.setup.setup import *

def main():
    # Connection to synthea10k
    conn = connect_db()

    cs = ConceptSet(
        conn=conn,
        conceptset_name="Diabetes Mellitus test",
        concept_ids=[201826, 201820],  # Real OMOP Concept IDs as an example (Condition)
        concept_names=["Diabetes mellitus"],
        include_descendants=True
    )

    # Build DataFrame
    df = cs.build()

    # Show results
    print("\n ConceptSet creado correctamente.")
    print(f"ConceptSet ID: {cs.conceptset_id}")
    print(f"ConceptSet Name: {cs.get_name()}")
    print(f"Número de conceptos: {len(df)}")
    print("\n--- Vista previa del ConceptSet ---")
    print(df.head(10))

    # Show global registry
    print("\n--- Registro global de ConceptSets ---")
    print(conceptset_registry)


if __name__ == "__main__":
    main()
