from dataclasses import dataclass
from typing import List, Optional
from pysynthea.cohorts.exit.censoring_events import CensoringEvent
from pysynthea.cohorts.exit.event_persistence import EventPersistence



@dataclass
class CohortExitEvent:
    event_persistence: EventPersistence
    censoring_events: Optional[List[CensoringEvent]] = None
    
    def describe(self)->List[str]:
        desc = []
        # EventPersistence description
        desc.extend(self.event_persistence.describe())
        # List of CensoringEvents description
        if self.censoring_events:
            for ce in self.censoring_events:
                desc.extend(ce.describe())
        return desc


    