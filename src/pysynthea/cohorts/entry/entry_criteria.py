from dataclasses import dataclass
from typing import Literal, Optional
from pysynthea.cohorts.criteria.subgroup_criteria import Subgroup_Criteria
from pysynthea.cohorts.criteria.inclusion_criteria import Inclusion_Criteria

"""
Module: entry_event_type

This module defines the 'EntryCriteria' class, which encapsulates all the
configuration rules needed to determine how individuals enter an ATLAS-style
cohort. These rules follow the standard logic used by OHDSI ATLAS and include
observation requirements, event limitations, and optional subgroup restrictions.

Dependencies
------------
This module requires two additional modules that define optional restrictions
applied when 'restrict_initial' is set to True:

subgroup_criteria.py
inclusion_criteria.py

    
Both dependencies are automatically instantiated inside `EntryCriteria`
when `restrict_initial`='True'.

Typical usage
-------------
Two specific examples will be given, in case restrict_initial is set to True.
from pysynthea.cohorts.entry_event_type import EntryCriteria
from .subgroup_criteria import Subgroup_Criteria
from .inclusion_criteria import Inclusion_Criteria

1. restrict_initial is False
    criteria = EntryCriteria(
        limit_initial_events_per_person="earliest event",
        continuous_obs_before=30,
        continuous_obs_after=0
    )

2. restrict_initial is True
    criteria_with_subgroups = EntryCriteria(
        limit_initial_events_per_person="all events",
        continuous_obs_before=90,
        continuous_obs_after=30,
        restrict_initial=True
    )

# `criteria_list_crit` and `inclusion_criteria` are automatically initialized.
print(criteria_with_subgroups.criteria_list_crit)
print(criteria_with_subgroups.inclusion_criteria)

"""

""" Types created to define attributes in EntryCriteria. Values are predefined in ATLAS."""
Window = Literal[0,1,7,14,21,30,60,90,120,180,365,548,730,1095]
LimitEvent = Literal ["all events", "earliest event", "latest event"]

@dataclass
class EntryCriteria:
    """
    Represents the criteria for entering a cohort in ATLAS.

    These settings determine how candidate entry events are selected,
    whether they must satisfy observation windows, and whether filtering
    based on additional sub-criteria is applied.
    
    Attributes
    ----------
    limit_initial_events_per_person: LimitEvent
        How many qualifying entry events per person to consider.
        Default is "all events".
    continuous_obs_before: Window
        Required continuous observation time before the event (in days).
        Default is 0.
    continuous_obs_after: Window
        Required continuous observation time after the event (in days).
        Default is 0.
    restrict_initial: bool
        Whether additional filtering rules must be applied.
        If True, extra criteria objects will be automatically created. These are 
        imported from the Subgroup_Criteria and Inclusion_Criteria classes.
        Default is False.
    criteria_list_crit: Subgroup_Criteria, optional
        Additional subgroup criteria applied when 'restrict_initial' is True.
        Initialized automatically only when 'restrict_initial' is True
    inclusion_criteria: Inclusion_Criteria, optional
        Inclusion criteria for restricting entry events when
        'restrict_initial' is True. 
        Initialized automatically only when 'restrict_initial' is True.
    """
    
    # Mandatory CohortEntryEvent configuration 
    limit_initial_events_per_person: LimitEvent = "all events"
    continuous_obs_before: Window = 0
    continuous_obs_after: Window = 0

    # Additional configuration. Only if restrict_initial_events is True
    restrict_initial: bool = False

    # Imported from Criteria, when restrict_initial_events is True
    criteria_list_crit: Optional[Subgroup_Criteria] = None # List of criterions and having_x_of_the_following_criteria
    inclusion_criteria: Optional[Inclusion_Criteria] = None # limit_qualifying_events_to

    def __post_init__(self):
        """
        Initializes `criteria_list_crit` and `inclusion_criteria` automatically
        if `restrict_initial` is True. 

        This ensures that the optional attributes are always set to
        valid default objects when additional restrictions are required.

        Notes
        -----
        - Do not manually set `criteria_list_crit` or `inclusion_criteria`
        if `restrict_initial` is True, as they will be overwritten.
        """
        if self.restrict_initial:
            self.criteria_list_crit = Subgroup_Criteria()
            self.inclusion_criteria = Inclusion_Criteria()


