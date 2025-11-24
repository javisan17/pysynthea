from dataclasses import dataclass
from typing import List, Literal, Optional
from pysynthea.concept_set.concept_class import*

"""
Module: event_persistence
-------------------------

This module defines classes representing event persistence in a CohortExitEvent
for use in cohort definitions in ATLAS.

EventPersistence determines how long an event persists in a cohort and is
implemented via three predefined types, each represented by a subclass:

    - EndOfContinuousObservation
    - FixedDuration
    - EndOfDrugExposure

Additionally, it defines a helper type 'Window' representing fixed duration
options used across persistence types.

Classes
--------
EventPersistence
EndOfContinuousObservation
FixedDuration
EndOfDrugExposure

Dependencies
------------
concept_class.py

Typical usage
-------------
Three specific examples are given to illustrate the usage of the subclasses.

from pysynthea.concept_set.concept_class import ConceptSet
from pysynthea.setup.setup.py import connect_db()
from event_persistence import EndOfContinuousObservation, FixedDuration, EndOfDrugExposure

conn = connect_db()

# Example ConceptSet for drugs
drug_cs = ConceptSet(
    conn=conn,  # Replace with actual DB connection
    conceptset_name="Metformin",
    concept_ids=[1111, 2222],
    concept_names=["Metformin"],
    include_descendants=True
)

1. Persistence until end of continuous observation
    obs_persist = EndOfContinuousObservation()
    print(obs_persist.describe())

2. Persistence for fixed duration
    fixed_persist = FixedDuration(offset_from="start date", offset_days=30)
    print(fixed_persist.describe())

3. Persistence until end of drug exposure
    drug_persist = EndOfDrugExposure(
        drug_concept_set=drug_cs,
        persistence_window=5,
        surveillance_window=3,
        force_duration=True,
        drug_exposure_window=10
    )
    print(drug_persist.describe())
"""

@dataclass
class EventPersistence:
    """
    Base class for event persistence in a CohortExitEvent.

    Determines how long an event persists in a cohort. Implemented via three 
    predefined types, each represented by a subclass.

    Methods
    -------
    persistence_type() -> str
        Returns the type of persistence.
    describe() -> List[str]
        Returns a textual description of the event's persistence.
    """

    def persistence_type(self) -> str:
        """
        Indicates the type of persistence.

        Returns
        -------
            str
                Type of persistence. One of the three predefined options defined
                in subclasses.
        """
        return

    def describe(self) -> List[str]:
        """
        Generates a textual description of the EventPersistence, including its type.

        Returns
        -------
            List[str]
                Human-readable description of the persistence type.
        """
        event_desc = [f"Event will persist until: {self.persistence_type()}"]
        return event_desc


""" Type created to define durations in EventPersistence subclasses. Values are predefined in ATLAS."""
Window = Literal[0,1,7,14,21,30,60,90,120,180,365,548,730,1095]



@dataclass
class EndOfContinuousObservation(EventPersistence):
    """
    EventPersistence subclass representing persistence until the end of continuous observation.
    This type has no extra attributes beyond those inherited from EventPersistence.

    Methods
    -------
    persistence_type() -> str
        Returns a string specifying the type of persistence.
    
    Notes
    -----
    Inherits from EventPersistence.
    """
    def persistence_type(self) -> str:
        """
        Returns the type of persistence.

        Returns
        -------
        str
            Indicates that the event persists until the end of continuous observation.
        """
        return "end of continuous observation"



@dataclass
class FixedDuration(EventPersistence):
    """
    EventPersistence subclass representing persistence until fixed duration relative to initial event.

    Attributes
    ----------
    offset_from: Literal["start date", "end date"]
        Indicates whether the offset is calculated from the start or end of the event.
        Default is "start date".
    offset_days: Window
        Number of days for the fixed duration offset. Options represented by a Window object.
        Default is 0.

    Methods
    -------
    persistence_type() -> str
        Returns a string specifying the type of persistence.
    describe() -> List[str]
        Returns a textual description including persistence type and offset information.

    Notes
    -----
    Inherits from EventPersistence.
    """
    offset_from: Literal["start date", "end date"] = "start date"
    offset_days : Window = 0

    def persistence_type(self) -> str:
        """
        Returns the type of persistence.

        Returns
        -------
        str
            Indicates that the event persists until fixed duration relative to initial event.
        
        """
        return "fixed duration relative to initial event"
    
    def describe(self) -> List[str]:
        """
        Generates a textual description of the persistence, including offset information.

        Returns
        -------
        List[str]
            Human-readable description of the event persistence type,
            offset reference, and duration in days.
        """
        event_desc = super().describe()
        event_desc.append(f"Offset from: {self.offset_from}" )
        event_desc.append(f"Number of days offset: {self.offset_days} days")
        return event_desc

@dataclass
class EndOfDrugExposure(EventPersistence):
    """
    EventPersistence subclass representing persistence until end of a continuous drug exposure.

    Attributes
    ----------
    drug_concept_set : ConceptSet
        ConceptSet object representing the drug(s) of interest.
    drug_concept_set_name : str
        Name of the drug ConceptSet, populated automatically from 'drug_concept_set'. Do not set it automatically.
    surveillance_window : Window
        Additional days added after the end of drug exposure to extend surveillance.
        Default is 0.
    persistence_window : Window
        Maximum number of days allowed between consecutive exposure records when defining continuous exposure.
        Default is 0.
    force_duration : boolean, optional
        If True, forces all exposures to use 'drug_exposure_window' as the duration.
        If False, uses days supply and exposure end date for exposure duration.
        Default is False.
    drug_exposure_window : Window, optional
        Number of days to enforce as exposure duration when 'force_duration' is True.
        Default is 1.

    Methods
    -------
    persistence_type() -> str
        Returns a string specifying the type of persistence.
    describe() -> List[str]
        Returns a textual description including persistence type, concept set,
        persistence window, surveillance window, and forced duration settings.

    Notes
    -----
    Inherits from EventPersistence.
    """
    drug_concept_set : ConceptSet
    drug_concept_set_name : str = field(init=False)
    surveillance_window: Window = 0
    persistence_window: Window = 0
    force_duration: Optional[bool] = False
    drug_exposure_window: Optional[Window] = 1

    def __post_init__(self):
        if isinstance(self.drug_concept_set, ConceptSet):
            self.drug_concept_set_name = self.drug_concept_set.get_concept_set_name()
        else:
            raise TypeError("drug_concept_set debe ser una instancia de ConceptSet")


    def persistence_type(self) -> str:
        """
        Returns the type of persistence.

        Returns
        -------
        str
            Indicates that the event persists until end of a continuous drug exposure.
        """
        return "end of a continuous drug exposure"
    
    def describe(self):
        """
         Generate a textual description of the EndOfDrugExposure persistence.

        Returns
        -------
        List[str]
            Human-readable description of persistence type, drug concept set, persistence 
            and surveillance windows and forced duration settings if applicable
        """
        event_desc= super().describe()
        event_desc.append(f"Concept set containing the drug(s) of interest: {self.drug_concept_set_name}")
        event_desc.append(f"Persistence window: allow for a maximum of {self.persistence_window} days between exposure records when inferring the era of persistence exposure")
        event_desc.append(f"Surveillance window: add {self.surveillance_window} days to the end of the era of persistence exposure as an additional period of surveillance prior to cohort exit.")
        if self.force_duration:
            event_desc.append(f"Force drug exposure days supply to: {self.drug_exposure_window} days.") 
        elif self.force_duration is False:
            event_desc.append(f"Use days supply and exposure end date for exposure duration.")
        
        return event_desc