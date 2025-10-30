import pandas as pd
from dataclasses import dataclass

class ConceptSet:
    """
    Representa un conjunto de conceptos (Concept Set).
    Contiene los conceptos base, los descendientes (opcional), y metadatos.
    """

    def __init__(self, conceptset_id, name=None, include_descendants=False):
        self.conceptset_id = conceptset_id
        self.name = name or f"ConceptSet_{conceptset_id}"
        self.include_descendants = include_descendants
        self.base_concepts = pd.DataFrame()
        self.descendants = pd.DataFrame()
        self.final_df = pd.DataFrame()

    def build(self, conn, concept_ids=None, concept_names=None, fetchers=None):
        """
        Construye el ConceptSet usando IDs y/o nombres.
        """
        if not fetchers:
            raise ValueError("Debe pasarse un diccionario con funciones de acceso (fetchers).")

        fetch_by_ids = fetchers["by_ids"]
        fetch_by_names = fetchers["by_names"]
        fetch_desc = fetchers["descendants"]

        concept_ids = concept_ids or []
        concept_names = concept_names or []

        # Recuperar conceptos base por nombre o id
        name_df = fetch_by_names(conn, concept_names)
        id_df = fetch_by_ids(conn, concept_ids)

        # Mezclar ambos
        all_ids = list(concept_ids) + name_df["concept_id"].tolist()
        self.base_concepts = pd.concat([name_df, id_df], ignore_index=True).drop_duplicates(subset=["concept_id"])

        if self.include_descendants and all_ids:
            self.descendants = fetch_desc(conn, all_ids)

        # Unificar todo
        combined = pd.concat([self.base_concepts, self.descendants], ignore_index=True).drop_duplicates(subset=["concept_id"])
        combined["conceptset_id"] = self.conceptset_id

        self.final_df = combined[["conceptset_id"] + [c for c in combined.columns if c != "conceptset_id"]]

    def export_csv(self, path=None):
        """
        Exporta el ConceptSet a CSV.
        """
        if self.final_df.empty:
            print("ConceptSet vacío, nada que exportar.")
            return
        path = path or f"{self.name}.csv"
        self.final_df.to_csv(path, index=False)
        print(f"ConceptSet exportado a {path}")

    def __repr__(self):
        return f"<ConceptSet id={self.conceptset_id}, name='{self.name}', concepts={len(self.final_df)}>"

class Concept_Set:
    """
    
    """

    def __init__(self, conn, concept_ids, concept_names, include_descendants=False):
        self.conn=conn




