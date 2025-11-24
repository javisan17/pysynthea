import pandas as pd

"""
Tools for retrieving OMOP concepts and building concept sets. These are used in the ConceptSet class.

This module provides helper functions to:
- Retrieve concepts by name from the OMOP 'concept' table.
- Retrieve concepts by concept_id.
- Retrieve descendant concepts using the 'concept_ancestor' table.
- Combine these into a final concept set DataFrame.

Dependencies
------------
pandas
setup.py module must be imported

Typical usage
-------------
from yourpackage.utils_concept_set import *
from yourpackage.db import connect_db
import pandas as pd

conn = connect_db()
name_df = concepts_by_names(conn, ["Diabetes mellitus"])
id_df = concepts_by_ids(conn, [201820])
descendants_df = get_descendants(conn, [201820])
conceptset = final_conceptset_df(
    name_df, 
    id_df, 
    descendants_df, 
    conceptset_id=1)

All functions return pandas DataFrames.

"""

def concepts_by_names(conn, concept_names):
    """
    Retrieve all concepts from the 'concept' table that match the given list of concept names.

    Parameters
    ----------
    conn : database connection
        Open connection to the OMOP database.
    concept_names : list[str]
        List of concept names to search for.

    Returns
    -------
    pandas.DataFrame
        Rows from the 'concept' table that match the provided names.
    """

    if not concept_names:
        return

    names_str = "', '".join(concept_names)
    query_names = f"""
        SELECT *
        FROM concept
        WHERE concept_name IN ('{names_str}')
    """
    return pd.read_sql(query_names, conn)



def concepts_by_ids(conn, concept_ids):
    """
    Retrieve all concepts from the 'concept' table that match the given list of concept IDs.

    Parameters
    ----------
    conn : database connection
        Open connection to the OMOP database.
    concept_ids : list[int]
        List of concept ids to search for.
    
    Returns
    -------
    pandas.DataFrame
        Rows from the 'concept' table that match the provided names.
    """

    if not concept_ids:
        return

    ids_str = ",".join(map(str, concept_ids))
    query_ids = f"""
        SELECT *
        FROM concept
        WHERE concept_id IN ({ids_str})
    """
    return pd.read_sql(query_ids, conn)



def get_descendants(conn, concept_ids):
    """
    Retrieve all descendant concepts related to the given ancestor concept IDs from the 'concept_ancestor' table.

    Parameters
    ----------
    conn : database connection
        Open connection to the OMOP database.
    concept_ids : list[int]
        List of ancestor concept IDs for which descendants will be retrieved.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the descendant concepts with all the columns
        from the OMOP 'concept' table. Each row corresponds to a concept
        whose concept_id is a descendant of one of the provided ancestor IDs.
    """

    ids_str = ",".join(map(str, concept_ids))
    query_descendats = f"""
        SELECT c.*
        FROM concept_ancestor ca
        JOIN concept c
        ON c.concept_id = ca.descendant_concept_id
        WHERE ca.ancestor_concept_id IN ({ids_str})
    """
    return pd.read_sql(query_descendats, conn)



def final_conceptset_df(name_df, id_df, descendants_df, conceptset_id):
    """
    Combine concept DataFrames, remove duplicates, assign a concept set ID, and return the final unified DataFrame.

    Parameters
    ----------
    name_df: pandas.DataFrame
        DataFrame containing concepts retrieved by concept names.
    id_df: pandas.DataFrame
        DataFrame containing concepts retrieved by concept IDs.
    descendants_df: pandas.DataFrame
        DataFrame containing descendant concepts of the selected IDs.
    conceptset_id: int
        Identifier assigned to the resulting concept set.

    Returns
    -------
    pandas.DataFrame
        Final concept set DataFrame. The `conceptset_id` column is placed first
        and identifies the concept set. Contains all concepts from the three
        DataFrames with duplicates (by concept_id) removed.
    """

    df = pd.concat([name_df, id_df, descendants_df], ignore_index=True).drop_duplicates(subset=["concept_id"], ignore_index=True)
    df["conceptset_id"] = conceptset_id
    cols = ["conceptset_id"] + [c for c in df.columns if c != "conceptset_id"]
    return df[cols]


# def export_csv(df):
#     """
#     df.to_csv('name.csv', index=False)
#     """
    
#     pass