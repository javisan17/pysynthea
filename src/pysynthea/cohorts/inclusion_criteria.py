from dataclasses import dataclass
from typing import Literal

from .group_criteria import *


"""
Father father class
"""
@dataclass
class Inclusion_Criteria:
    named_criteria: list[Named_Group_Criteria] = field(default_factory=list)
    limit_qualifying_events_to: Literal["all events", "earliest event", "latest event"] = "earliest event"

    def add_named_criteria(self, group: Named_Group_Criteria):
        self.named_criteria.append(group)

    def get_named_criteria(self):
        return self.named_criteria
