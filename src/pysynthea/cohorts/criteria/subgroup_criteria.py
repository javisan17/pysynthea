from dataclasses import dataclass, field
from typing import Literal, List
from .fathers_criteria import *


"""
Module: subgroup_criteria

This module defines the Subgroup_Criteria class, which allows grouping multiple 
Criteria objects under a single logical unit for use in ATLAS-like cohort definitions.
Each subgroup can specify how many of its criteria must be satisfied ("all", "any", 
"at least", "at most").

Dependencies
------------
fathers_criteria.py

Typical usage
from .fathers_criteria import Criteria
from .subgroup_criteria import Subgroup_Criteria

# Create subgroup criteria
subgroup = Subgroup_Criteria(having_x_of_the_following_criteria="all")
criterion1 = Criteria()
criterion2 = Criteria()

subgroup.add_criterion(criterion1)
subgroup.add_criterion(criterion2)

all_criteria = subgroup.get_criteria()
"""

@dataclass
class Subgroup_Criteria:
    """
    Represents a subgroup of criteria within a Named_Group_Criteria.

    Attributes
    ----------
    having_x_of_the_following_criteria: Literal["all", "any", "at least", "at most"]
        Specifies how many of the criteria in the list must be satisfied.
        Default is "all".
    criteria: List[Criteria]
        List of Criteria objects included in this subgroup.

    Methods
    -------
    add_criterion(criterion: Criteria)
        Adds a new Criteria object to the subgroup.
    get_criteria() -> List[Criteria]
        Returns the list of Criteria objects contained in this subgroup.
    """

    having_x_of_the_following_criteria: Literal["all", "any", "at least", "at most"] = "all"
    criteria: List[Criteria] = field(default_factory=list)


    def add_criterion(self, criterion: Criteria):
        """
        Adds a Criteria object to the subgroup.

        Parameters
        ----------
        criterion : Criteria
            The criterion to be added to the subgroup.
        """
        self.criteria.append(criterion)


    def get_criteria(self):
        """
        Returns the list of criteria in this subgroup.

        Returns
        -------
        List[Criteria]
            The list of Criteria objects added to this subgroup.
        """
        return self.criteria