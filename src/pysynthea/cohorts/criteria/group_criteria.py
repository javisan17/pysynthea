from dataclasses import dataclass, field
from .subgroup_criteria import *

"""
Module: group_criteria

This module defines the Named_Group_Criteria class, a container 
for user-defined criteria groups in ATLAS-like cohort definitions. 
It stores a name, a description, and a list of Subgroup_Criteria objects, 
allowing related criteria to be organized and managed as a single logical unit

Dependencies
------------
subgroup_criteria.py

Typical usage
-------------
from pysynthea.criteria.group_criteria import Named_Group_Criteria
from pysynthea.criteria.subgroup_criteria import Subgroup_Criteria

1. Create one or more Subgroup_Criteria objects
    subgroup1 = Subgroup_Criteria()
    subgroup2 = Subgroup_Criteria()

2. Create a Named_Group_Criteria to group them under a user-defined label
    ngc = Named_Group_Criteria(
        name="Baseline Restrictions",
        description="Set of subgroup rules applied at cohort entry.")

3. Add subgroup criteria to the named group
    ngc.add_group_criteria(subgroup1)
    ngc.add_group_criteria(subgroup2)

4. Retrieve all subgroup criteria associated with this named group
    criteria_list = ngc.get_group_criteria()
    print(criteria_list)
"""

@dataclass
class Named_Group_Criteria:
    """
    Container for user-defined criteria groups in ATLAS-like cohort definitions.
    It includes a name and a description for the criteria group, as well as a list
    that contains the individual criterions.

    Attributes
    ----------
    name: str
        Name given to the criteria
        Default is an empty string.
    description: str
        Description of said criteria.
        Default is an empty string.
    groups_criteria: List[Subgroup_Criteria]
        List of Subgroup_Criteria that are included in this criteria.
        A list must be given, only if only one item is included.
    
    Methods
    -------
    add_group_criteria(group_criteria: Subgroup_Criteria)
        Adds a new Subgroup_Criteria to the named group.
    get_group_criteria() -> List[Subgroup_Criteria]
        Returns a list of Subgroup_Criteria that belong to the named group. 
    """
    name: str = ""
    description: str = ""
    groups_criteria: List[Subgroup_Criteria] = field(default_factory=list)

    

    def add_group_criteria(self, group_criteria: Subgroup_Criteria):
        """
        Adds a new Subgroup_Criteria to the 'groups_criteria' list.

        Parameters
        ----------
        group_criteria: Subgroup_Criteria
            The Subgroup_Criteria instance to add to this named group.
        """
        self.groups_criteria.append(group_criteria)

    def get_group_criteria(self):
        """
        Returns
        -------
        List[Subgroup_Criteria]
            Returns the list of Subgroup_Criteria that are included in 'groups_criteria'.
        """
        return self.groups_criteria