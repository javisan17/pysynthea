import pandas as pd
from .utils_concept_set import *

# Returns the desired Concept Set's DataFrame  
    # DataFrame's columns include those from the CONCEPT table and an additional one with the conceptset_id 
    # If descendants are wanted you must specify it when using the function

def get_concept_set(conn, conceptset_id, concept_ids=None, concept_names=None, include_descendants=False):
    """
    Build and return a complete concept set DataFrame by combining concepts from given IDs and/or names, optionally including their descendants.
    """

    if concept_ids is None:
        concept_ids = []
    if concept_names is None:
        concept_names = []

    if not concept_ids and not concept_names:
        print("No concept_ids or concept_names were given.")
        return

    # Get IDs from names
    name_df = concepts_by_names(conn=conn, concept_names=concept_names)

    # Get base and descendant concepts
    id_df = concepts_by_ids(conn=conn, concept_ids=concept_ids)

    #Id list
    concept_ids.extend(name_df["concept_id"].tolist())

    if not concept_ids:
        print("Empty list, no concepts could be found for this Concept Set.")
        return

    # Get descendants of every concept
    descendants_df = include_ancestors(conn=conn, concept_ids=concept_ids) if include_descendants else pd.DataFrame()

    # 3. Merge results and format
    final_df = final_conceptset_df(name_df=name_df, id_df=id_df, descendants_df=descendants_df, conceptset_id=conceptset_id)

    return final_df