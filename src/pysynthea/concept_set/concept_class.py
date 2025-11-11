from dataclasses import dataclass, field
from typing import List, Optional
from itertools import count
import pandas as pd
from .utils_concept_set import *

# Generates ids automatically to avoid repetition
_conceptset_id_gen = count(1)

# Global registry
conceptset_registry = pd.DataFrame(columns=["conceptset_id", "conceptset_name"])

@dataclass
class ConceptSet:
    conn: any                              # conexión a BD
    conceptset_name: str                   # MUST give ConceptSet name
    concept_ids: Optional[List[int]] = field(default_factory=list) # Must be given in a list, even when only one
    concept_names: Optional[List[str]] = field(default_factory=list) # Must be given in a list, even when only one
    include_descendants: bool = False
    conceptset_id: int = field(init=False) 
    concepts_df: Optional[pd.DataFrame] = field(default=None, init=False)

    def __post_init__(self):
        self.conceptset_id = next(_conceptset_id_gen)

        global conceptset_registry
        conceptset_registry.loc[len(conceptset_registry)] = [
            self.conceptset_id, self.conceptset_name
        ]

    
    def build(self)->pd.DataFrame:
        """Builds ConceptSet DataFrame with the utils functions"""
        
        if not self.concept_ids and not self.concept_names:
            raise ValueError("You must provide at least one concept_id or concept_name.")
        
        # Get IDs from names
        name_df = concepts_by_names(self.conn, self.concept_names)

        # Get base and descendant concepts
        id_df = concepts_by_ids(self.conn, self.concept_ids) 

        # id list
        if not name_df.empty:
            self.concept_ids.extend(name_df["concept_id"].tolist())
        
        # Remove duplicates from the id list 
        self.concept_ids = list(set(self.concept_ids))

        # Descendants
        descendants = (
        get_descendants(self.conn, self.concept_ids)
        if self.include_descendants else pd.DataFrame()
        )


        # Create final ConceptSet
        self.concepts_df = final_conceptset_df(
            name_df=name_df,
            id_df=id_df,
            descendants_df=descendants,
            conceptset_id=self.conceptset_id
        )

        return self.concepts_df
    
    """ConceptSet name getter"""
    def get_concept_set_name(self) -> str:
        return self.conceptset_name