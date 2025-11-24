from dataclasses import dataclass
from typing import List, Optional
from .entry_event_type import EntryEvent
from .entry_criteria import EntryCriteria

"""
Module: cohort_entry_event

This module contains the CohortEntryEvent class,
which represents the cohort entry event section in ATLAS.

It defines the criteria for entering a cohort, which include:
    - Optional entry events (`entry_events`) that may cause entry to the cohort.
    - The criteria (`entry_criteria`) that constrain and filter the events that should be considered for the entry.

Dependencies
------------
entry_event_type.py
entry_criteria.py

Typical usage
------------

from pysynthea.cohorts.cohort_entry_event import CohortEntryEvent
from pysynthea.cohorts.entry_event_type import EntryEvent
from pysynthea.cohorts.entry_criteria import EntryCriteria

1. Entry criteria
    entry_criteria = EntryCriteria(
        limit_initial_events_per_person="earliest event",
        continuous_obs_before=30,
        continuous_obs_after=30)

2.  CohortEntryEvent without EntryEvents
    cohort_entry = CohortEntryEvent(
        entry_events=None,
        entry_criteria=entry_criteria)
    print(cohort_entry.describe())

3. CohortEntryEvent with EntryEvents
    event1 = EntryEvent(event_type="condition occurrence")
    cohort_entry_with_events = CohortEntryEvent(
        entry_events=[event1],
        entry_criteria=entry_criteria)
    print(cohort_entry_with_events.describe())
"""

@dataclass
class CohortEntryEvent:
    """
    Represents a Cohort Entry Event in ATLAS.
    This class defines the criteria to enter a cohort. It includes:
        - A list of entry events (`entry_events`) that may qualify a person.
        - Entry-level criteria (`entry_criteria`) that constrain or filter
          which events can be considered valid cohort entry points.
    
    Parameters
    ----------
    entry_events: List[EntryEvent], Optional
        List of EntryEvents describing which events qualify as potential cohort entry events.
    entry_criteria: EntryCriteria
        Object defining observation windows, event limits, and optional
        subgroup/inclusion restrictions applied to entry events.

    Methods
    -------
    describe() -> str
        Returns a human-readable description of the entry events and
        the associated entry criteria.
    """
    entry_events : Optional[List[EntryEvent]] # mirar si poner Optional o no 
    entry_criteria : EntryCriteria

    def describe(self)->List[str]:
        """
        Generates a human-readable description of the Cohort Entry Event.

        The description includes:
            - The textual descriptions of each EntryEvent.
            - Observation window requirements (before/after index date).
            - How initial events per person are limited.
            - Additional subgroup/inclusion criteria, if 'restrict_initial is enabled.

        Returns
        -------
        str
            A multi-line string describing the full set of entry rules
            that define how a person enters the cohort.
        """
        events_desc = []
        if self.entry_events:
            for event in self.entry_events:
                events_desc.extend(event.describe())

        # Mandatory description of EntryCriteria
        criteria_desc = []
        criteria_desc.append(
            f"With continuous observation of at least "
            f"{self.entry_criteria.continuous_obs_before} days before and "
            f"{self.entry_criteria.continuous_obs_after} days after event index date."
        )
        criteria_desc.append(f"Limit initial events to: {self.entry_criteria.limit_initial_events_per_person} per person.")

        # Additional description, only if restrict_initial is True
        if self.entry_criteria.restrict_initial and self.entry_criteria.criteria_list_crit:
            having = self.entry_criteria.criteria_list_crit.having_x_of_the_following_criteria
            criteria_desc.append(f"Restrict initial events to: having {having} of the following criteria:")
            for i, crit in enumerate(self.entry_criteria.criteria_list_crit.criteria, start=1):
                criteria_desc.append(f"  - Criterion {i} ({type(crit).__name__})")

        return "\n".join(events_desc + criteria_desc)