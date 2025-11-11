import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "src"))

from pysynthea import concept_set
from pysynthea.cohorts.entry.cohort_entry_event import *
from pysynthea.cohorts.entry.entry_criteria import *
from pysynthea.cohorts.entry.entry_event_type import *
from pysynthea.cohorts.criteria.criteria import *
from pysynthea.cohorts.criteria.subgroup_criteria import *
from pysynthea.cohorts.criteria.inclusion_criteria import *
from pysynthea.setup.setup import *


def main():

    # Connetion to synthea10k
    conn = connect_db()

    # Needed ConceptSets 
    visit= ConceptSet(conn=conn, conceptset_name="ER visit", concept_names=["Emergency Room Visit"], include_descendants=True) 
    procedure= ConceptSet(conn= conn, conceptset_name="C-Section", concept_names="Cesarean section", include_descendants=True)
    diabetes = ConceptSet(conn=conn, conceptset_name="Diabetes", concept_names=["Diabetes"], include_descendants=True)


    # EntryEvents
    entry1=ObservationPeriodEntry()
    entry2=VisitOccurrenceEntry(concept_set=visit)
    entry3=ProcedureOccurrenceEntry(concept_set=procedure)
    entry4=PayerPlanPeriodEntry()

    # Criteria for EntryCriteria --> EntryCriteria need an Options object 
    # Options 
    opts = Options(
    how_occurrence="at least",
    amount_occurrence=3,
    using_occurrence="using all",
    time_event="event starts",
    time_window_value="all",
    time_window_relation="before",
    reference_window_value=7,
    reference_window_relation="before",
    index_date_point="index end date",
    allow_events_from_outside_observation_period=False)

    
    # Options_Concept
    cond1 = Add_Condition_Era(concept_set=diabetes, options=opts)
    # Options_Concept_Extra
    cond2 = Add_Visit_Occurrence(concept_set=visit, options=opts)
    # Options
    cond3 = Add_Procedure_Occurrence(concept_set= procedure, options= opts, restrict_to_the_same_visit_occurrence=False)

    subgr1 = Subgroup_Criteria(having_x_of_the_following_criteria="any", criteria=[cond1, cond2])
    subgr2= Subgroup_Criteria(criteria=[cond2, cond3])
    namedgrcrit1= Named_Group_Criteria(name="Group 1", description="Patients with Diabetes and ER Visits", groups_criteria=subgr1)
    namedgrcrit2 = Named_Group_Criteria(name="Group 2", description="Patients with an Emergency C-Section", groups_criteria=subgr2)
    inccrit1= Inclusion_Criteria(named_criteria= namedgrcrit1, limit_qualifying_events_to="earliest event")
    inccrit2=Inclusion_Criteria(named_criteria=namedgrcrit2)

    # EntryCriteria
    entrycrit1= EntryCriteria(limit_initial_events_per_person="latest event", continuous_obs_before=0, continuous_obs_after= 7, restrict_initial=True, criteria_list_crit=subgr2, inclusion_criteria=inccrit2)
    entrycrit2=EntryCriteria(limit_initial_events_per_person="all events", continuous_obs_after=365, continuous_obs_before=7, restrict_initial=True, criteria_list_crit=subgr1, inclusion_criteria=inccrit1)

    # Cohort definition 
    cohorte1= CohortEntryEvent(entry_events=[entry1, entry2, entry4], entry_criteria=entrycrit1)
    cohorte2= CohortEntryEvent(entry_events=[entry3], entry_criteria=entrycrit2)

    # Describe
    print("Cohorte 1:")
    print(cohorte1.describe())

    print("Cohorte 2:")
    print(cohorte2.describe())


    







if __name__ == '__main__':
    main()