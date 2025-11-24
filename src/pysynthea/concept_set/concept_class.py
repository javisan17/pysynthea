from dataclasses import dataclass, field
from typing import List, Optional
from itertools import count
import pandas as pd
from .utils_concept_set import *

"""
Module: concept_class.py

This module aims to represent ATLAS Concept Sets. Utils must be imported for a correct functionality.
It includes the ConceptSet class, as well as a global registry (pandas DataFrame). 
This register the ConceptSets IDs and names.

Classes
-------
ConceptSet

Dependencies
------------
utils_concept_set.py must be imported
pandas 
"""

# Generates ids automatically to avoid repetition
_conceptset_id_gen = count(1)

# Global registry
conceptset_registry = pd.DataFrame(columns=["conceptset_id", "conceptset_name"])

@dataclass
class ConceptSet:
    """
    Represent a collection of OMOP concepts defined by concept IDs, concept names,
    and optionally their descendant concepts.

    This class provides a structured interface to:
    - Resolve concept names into concept IDs.
    - Retrieve full OMOP concepts from the 'concept' table.
    - Optionally include descendant concepts using the 'concept_ancestor' table.
    - Build a unified pandas DataFrame representing the complete ConceptSet.
    - Automatically register each ConceptSet with a unique internal ID.

    Parameters
    ----------
    conn: any
        Database connection object compatible with 'pandas.read_sql'.
    conceptset_name: str
        Name assigned to the ConceptSet. Must be set by the user.
    concept_ids: List[int], optional
        List of concept IDs. Must be provided as a list even if only one is given.
        Real OMOP IDs should be given.
    concept_names: List[str], optional
        List of concept names. Must be provided as a list even if only one is given.
    include_descendants: boolean
        If True, include all descendant concepts of the provided IDs.
    
            
    Attributes
    ----------
    conceptset_id: int
        Automatically generated unique identifier for the ConceptSet.
    concepts_df: pandas.DataFrame or None
        Final DataFrame containing all concepts belonging to this ConceptSet.
        Populated after calling the 'build()' method.

    Methods
    -------
    build() -> pandas.DataFrame
        Builds and returns the final DataFrame by retrieving concepts by names and IDs,
        optionally adding descendants, and consolidating them into a single structure.
    get_concept_set_name() -> str
        Returns the name of the ConceptSet

    Typical usage
    -------------
    from yourpackage.concept_set import ConceptSet
    from yourpackage.db import connect_db

    conn = connect_db()

    cs = ConceptSet(
        conn=conn,
        conceptset_name="Diabetes Mellitus",
        concept_ids=[201826, 201820],  # Real OMOP Concept IDs as an example (Condition)
        concept_names=["Diabetes mellitus"],
        include_descendants=True
    )

    diabetes = cs.build()
    diabetes.get_concept_set_name() # Would return Diabetes Mellitus
    """
    conn: any                              
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
        """
        Builds ConceptSet DataFrame with the utils functions.
        Optionally includes descendant concepts.


        Returns
        -------
        pandas.DataFrame
            Final DataFrame containing the complete ConceptSet.

        Raises
        ------
        ValueError
            If neither concept_ids nor concept_names are provided.
        """
        
        if not self.concept_ids and not self.concept_names:
            raise ValueError("You must provide at least one concept_id or concept_name.")
        
        # Get IDs from names
        name_df = concepts_by_names(self.conn, self.concept_names)

        # Get base and descendant concepts
        id_df = concepts_by_ids(self.conn, self.concept_ids) 

        # Update ID list with IDs resolved from names
        if not name_df.empty:
            self.concept_ids.extend(name_df["concept_id"].tolist())
        
        # Remove duplicates from the id list 
        self.concept_ids = list(set(self.concept_ids))

        # Optionally retrieve descendants
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
    
    

    def get_concept_set_name(self) -> str:
        """
        ConceptSet name getter

        Returns
        -------
        str
            A string describing the ConceptSet name.
        """
        return self.conceptset_name