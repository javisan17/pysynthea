from dataclasses import dataclass
from typing import Literal, List

from .group_criteria import *


"""
Module: inclusion_criteria.py

This module defines the Inclusion_Criteria class, which represents
the inclusion rules used to restrict or qualify cohort entry events
in ATLAS-like cohort definitions. It allows grouping user-defined
criteria and controlling how qualifying events are selected.

Dependencies
------------
group_criteria.py

Typical usage
-------------
from .group_criteria import Named_Group_Criteria
from .inclusion_criteria import Inclusion_Criteria

crit1 = Named_Group_Criteria(name="Diabetes group")
crit2 = Named_Group_Criteria(name="Hypertension group")

inclusion = Inclusion_Criteria(limit_qualifying_events_to="latest event")
inclusion.add_named_criteria(crit1)
inclusion.add_named_criteria(crit2)

selected = inclusion.get_named_criteria()
"""

@dataclass
class Inclusion_Criteria:
    """
    Represents a collection of user-defined named criteria used to
    restrict or qualify cohort entry events.

    Attributes
    ----------
    named_criteria: List[Named_Group_Criteria]
        A list of Named_Group_Criteria objects defined by the user.
        Each item groups one or more Subgroup_Criteria.
    limit_qualifying_events_to: Literal["all events", "earliest event", "latest event"]
        Determines how many of the qualifying events should be considered
        when applying inclusion logic.
        Default is "earliest event".

    Methods
    -------
    add_named_criteria(group: Named_Group_Criteria)
        Adds a new Named_Group_Criteria to the list.
    get_named_criteria()-> List[Named_Group_Criteria]
        Returns the list of named criteria included in the object.
    """
    named_criteria: List[Named_Group_Criteria] = field(default_factory=list)
    limit_qualifying_events_to: Literal["all events", "earliest event", "latest event"] = "earliest event"

    def add_named_criteria(self, group: Named_Group_Criteria):
        """
        Adds a Named_Group_Criteria object to the list of inclusion rules.

        Parameters
        ----------
        group : Named_Group_Criteria
            The criteria group to be included.
        """
        self.named_criteria.append(group)

    def get_named_criteria(self):
        """
        Returns
        -------
        List[Named_Group_Criteria]
            The list of user-defined named criteria.
        """
        return self.named_criteria
