
"""
TEST for the ConceptSet class. 
It verifies the correct creation of ConceptSets, including:
    - Connecting to a Synthea DuckDB database.
    - Creating a ConceptSet with specified concept IDs and concept names.
    - Optionally including descendant concepts.
    - Building the final ConceptSet DataFrame.
    - Printing key information such as ConceptSet ID, name, and number of concepts.
    - Displaying a preview of the DataFrame and the global ConceptSet registry.

Dependencies
------------
concept_class.py
setup.py

Notes
-----
- Requires the Synthea database to be available locally.
- Uses real OMOP concept IDs as examples (e.g., for Diabetes Mellitus).
- Intended as a standalone integration test, not a unit test.
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
    print("\n ConceptSet was created correctly.")
    print(f"ConceptSet ID: {cs.conceptset_id}")
    print(f"ConceptSet Name: {cs.get_name()}")
    print(f"Number of concepts: {len(df)}")
    print("\n--- ConceptSet Preview ---")
    print(df.head(10))

    # Show global registry
    print("\n--- ConceptSets Global Registry ---")
    print(conceptset_registry)


if __name__ == "__main__":
    main()
