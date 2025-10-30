from dataclasses import dataclass
from typing import Literal

from .group_criteria import *


"""
Father father class
"""
@dataclass
class Inclusion_Criteria:
    criteria: list[object: Named_Group_Criteria]
    limit_qualifying_events_to: Literal["all events", "earliest event", "latest event"]

    def add_group_inclusion_cirteria(self, group: object[Named_Group_Criteria]):
        self.criteria.append(group)
