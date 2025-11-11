import pandas as pd


def concepts_by_names(conn, concept_names):
    """
    Retrieve all concepts from the 'concept' table that match the given list of concept names.
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