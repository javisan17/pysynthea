import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "src"))

from pysynthea.setup.setup import *
from pysynthea.concept_set.concept_class import*
from pysynthea.cohorts.exit.event_persistence import *
from pysynthea.cohorts.exit.cohort_exit_event import *
from pysynthea.cohorts.exit.censoring_events import *


def main():

    # Connection to synthea10k
    conn = connect_db()


    # Needed ConceptSets 
    diabetes = ConceptSet(conn=conn, conceptset_name="Diabetes", concept_names=["Diabetes"], include_descendants=True)
    ibuprofen = ConceptSet(conn=conn, conceptset_name="Ibuprofen", concept_names=["Ibuprofen"], include_descendants=True)
    paracetamol = ConceptSet(conn=conn, conceptset_name="Paracetamol", concept_names=["Paracetamol"], include_descendants= True)

    # CensoringEvents
    censoring1 = ConditionEraExit(concept_set=diabetes)
    censoring2 = PayerPlanPeriodExit()
    censoring3 = DrugEraExit(concept_set=ibuprofen)

    # EventPersistence
    eventPers1 = FixedDuration(offset_from='start date', offset_days=30)
    print (eventPers1.describe())
    eventPers2 = EndOfDrugExposure(drug_concept_set= ibuprofen, 
                                   surveillance_window=60, 
                                   persistence_window=20, 
                                   force_duration=True, 
                                   drug_exposure_window=7)
    eventPers3 = EndOfDrugExposure(drug_concept_set= paracetamol,
                                   surveillance_window=60, 
                                   persistence_window=20, 
                                   force_duration=False)

    # Cohort definition
    cohort1 = CohortExitEvent(
        event_persistence=eventPers1,
        censoring_events=[censoring1, censoring2, censoring3]  
    )

    cohort2= CohortExitEvent(
        event_persistence=eventPers2,
        censoring_events=[censoring2]
    )
    
    # Describes
    print("Cohorte 1:")
    for line in cohort1.describe():
       print(line)

    print("\nCohorte 2:")
    for line in cohort2.describe():
        print(line)


if __name__ == '__main__':
    main()