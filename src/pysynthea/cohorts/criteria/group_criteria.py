from dataclasses import dataclass, field

from .subgroup_criteria import *


"""
De la padre puedes tener muchos named_groups
"""
@dataclass
class Named_Group_Criteria:
    name: str = ""
    description: str = ""
    groups_criteria: list[Subgroup_Criteria] = field(default_factory=list)

    """
    ###################### Preguntar si hay que poner getters y setters
    """

    def add_group_criteria(self, group_criteria: Subgroup_Criteria):
        self.groups_criteria.append(group_criteria)

    def get_group_criteria(self):
        return self.groups_criteria