from dataclasses import dataclass

from .subgroup_criteria import *


"""
De la padre puedes tener muchos named_groups
"""
@dataclass
class Named_Group_Criteria:
    name: str
    description: str
    groups_criteria: list[object[Subgroup_Criteria]]

    """
    ###################### Preguntar si hay que poner getters y setters
    """

    def add_group_criteria(self, group_criteria: object[Subgroup_Criteria]):
        self.groups_criteria.append(group_criteria)