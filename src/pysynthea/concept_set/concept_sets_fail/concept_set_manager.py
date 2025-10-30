from itertools import count
from .utils_concept_set import concepts_by_names, concepts_by_ids, include_ancestors
from .concept_set import ConceptSet

class ConceptSetManager:
    """
    Clase que gestiona la creación y carga de Concept Sets desde la base de datos.
    """

    _id_gen = count(1)

    def __init__(self, conn):
        self.conn = conn
        self.concept_sets = {}

    def create_concept_set(self, concept_ids=None, concept_names=None, include_descendants=False, name=None):
        """
        Crea un ConceptSet, lo construye y lo almacena internamente.
        """
        conceptset_id = next(self._id_gen)
        concept_set = ConceptSet(conceptset_id, name, include_descendants)

        concept_set.build(
            conn=self.conn,
            concept_ids=concept_ids,
            concept_names=concept_names,
            fetchers={
                "by_ids": concepts_by_ids,
                "by_names": concepts_by_names,
                "descendants": include_ancestors,
            }
        )

        self.concept_sets[conceptset_id] = concept_set
        return concept_set

    def get_concept_set(self, conceptset_id):
        """
        Recupera un ConceptSet ya creado.
        """
        return self.concept_sets.get(conceptset_id)

    def list_concept_sets(self):
        """
        Lista todos los ConceptSets creados hasta ahora.
        """
        return list(self.concept_sets.values())
