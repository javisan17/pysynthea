from dataclasses import dataclass
from typing import List, Literal, Optional
from pysynthea.cohorts.criteria.subgroup_criteria import Subgroup_Criteria
from pysynthea.cohorts.criteria.inclusion_criteria import Inclusion_Criteria


Window = Literal[0,1,7,14,21,30,60,90,120,180,365,548,730,1095]
LimitEvent = Literal ["all events", "earliest event", "latest event"]

@dataclass
class EntryCriteria:
    
    # Mandatory CohortEntryEvent configuration 
    limit_initial_events_per_person: LimitEvent = "all events"
    continuous_obs_before: Window = 0
    continuous_obs_after: Window = 0

    # Additional configuration. Only if restrict_initial_events is True
    restrict_initial: bool = False

    # Imported from Criteria, when restrict_initial_events is True
    criteria_list_crit : Optional[Subgroup_Criteria] = None # lista de criterios y having...
    inclusion_criteria: Optional[Inclusion_Criteria] = None # limit events to...

    def __post_init__(self):
        if self.restrict_initial:
            self.criteria_list_crit = Subgroup_Criteria()
            self.inclusion_criteria = Inclusion_Criteria()


