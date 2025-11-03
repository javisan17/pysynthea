from dataclasses import dataclass, field
from typing import Literal

from .fathers_criteria import *


"""
Dentro de una named_group puedes tener muchos subgroups
"""
@dataclass
class Subgroup_Criteria:
    having_x_of_the_following_criteria: Literal["all", "any", "at least", "at most"] = "all"
    criteria: list[Criteria] = field(default_factory=list)

    def add_criterion(self, criterion: Criteria):
        self.criteria.append(criterion)

    def get_criteria(self):
        return self.criteria