from dataclasses import dataclass
from typing import List, Optional
from pysynthea.cohorts.exit.censoring_events import CensoringEvent
from pysynthea.cohorts.exit.event_persistence import EventPersistence

"""
Module: cohort_exit_event

This module represents the Cohort Exit section in an ATLAS Cohort.
It defines the criteria for leaving a cohort, which include:
    - The main event that determines persistence (`event_persistence`).
    - Optional censoring events (`censoring_events`) that may trigger early exit.

Dependencies
------------
event_persistence.py.
censoring_events.py

Typical usage
-------------

from pysynthea.cohorts.exit.cohort_exit_event import CohortExitEvent
from pysynthea.cohorts.exit.event_persistence import EventPersistence
from pysynthea.cohorts.exit.censoring_event import CensoringEvent

# Create EventPersistence object
ep = EventPersistence(...)  # configure your event persistence

# Create CensoringEvent objects
ce1 = CensoringEvent(...)
ce2 = CensoringEvent(...)

# Build CohortExitEvent with both persistence and censoring events
exit_event = CohortExitEvent(event_persistence=ep, censoring_events=[ce1, ce2])

# Get human-readable description
print(exit_event.describe())

"""

@dataclass
class CohortExitEvent:
    """
    Represents a Cohort Exit Event in ATLAS.
    This class defines the criteria for leaving a cohort. It includes:
        - The main event that determines persistence (`event_persistence`).
        - Optional censoring events (`censoring_events`) that may cause early exit.

    Parameters
    ----------
    event_persistence: EventPersistence
        Object describing how the event persists or is measured.
    censoring_events: List[CensoringEvent], optional
        List of events that would censor the cohort exit.
        Default is None.

    Methods
    -------
    describe() -> List[str]
        Returns textual descriptions of the exit event and all censoring events.
    """
    event_persistence: EventPersistence
    censoring_events: Optional[List[CensoringEvent]] = None
    
    def describe(self)->List[str]:
        """
        Generates a textual description of the Cohort Exit Event.
        It combines the description of the 'event_persistence' and all 'censoring_events' (if any exist).

        Returns
        ------- 
        List[str]
            A list of human-readable strings describing the event persistence
            and all censoring events that define the cohort exit criteria.
        """
        desc = []
        # EventPersistence description
        desc.extend(self.event_persistence.describe())
        # List of CensoringEvents description
        if self.censoring_events:
            for ce in self.censoring_events:
                desc.extend(ce.describe())
        return desc


    