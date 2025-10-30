from dataclasses import dataclass, field
from typing import Literal

from .fathers_criteria import *


"""
Dentro de una named_group puedes tener muchos subgroups
"""
@dataclass
class Subgroup_Criteria:
    having_x_of_the_following_criteria: Literal["all", "any", "at least", "at most"]
    criteria: list[object: Criteria] = field(default_factory=list)

    def add_criterion(self, criterion: object[Criteria]):
        self.criteria.append(criterion)