from dataclasses import dataclass
from typing import List
from .entry_event_type import EntryEvent
from .entry_criteria import EntryCriteria

@dataclass
class CohortEntryEvent:
    entry_events : List[EntryEvent]
    entry_criteria : EntryCriteria

    def describe(self)->List[str]:
        events_desc = []
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
