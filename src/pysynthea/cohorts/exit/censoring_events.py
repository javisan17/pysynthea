from dataclasses import dataclass, field
from typing import List, Optional
from pysynthea.concept_set.concept_class import*

"""
Module: censoring_events

Defines classes representing cohort exit censoring events in ATLAS.

There are two main types of censoring events:
1. Normal events that can have an associated ConceptSet.
2. Special events that do not have a ConceptSet (e.g., payer plan period).

The module provides:
- Base classes: CensoringEvent, CensoringEventNormal, SpecialCensoringEvent
- Subclasses for each event type (ConditionEraExit, DrugExposureExit, DeathExit, etc.)
- Methods for describing events in human-readable form.

Classes
-------
CensoringEvent
CensoringEventNormal and SpecialCensoringEvent
All their specific subclasses (ConditionEraExit, ConditionOccurrenceExit...)

Dependencies
------------
concept_class.py
"""

@dataclass 
class CensoringEvent:
    """
    Base class for events that may cause early exit from a cohort. There are two types of censoring events, represented by subclasses.
    Inherited by CensoringEventNormal and SpecialCensoringEvent.

    Attributes
    ----------
    event_type: str
        Type of censoring event.

    Methods
    -------
    article() -> str
        Returns the appropriate English article ("a" or "an") based on the event_type.
        It is later used in the describe() method.
    describe() -> List[str]
        Returns a textual description of the censoring event.
    """
    event_type:str

    def article(self) -> str:
        """
        Returns the appropriate English article ("a" or "an") based on the event_type.

        Returns
        -------
        str
           "a" or "an", depending on the first letter of 'event_type'. 
        """
        return "an" if self.event_type.startswith(("a", "e", "i", "o", "u")) else "a"
    
    def describe(self) -> List[str]:
        """
        Returns a basic description for a cohort exit event.

        Returns
        -------
        List[str]
            A list with a single string describing the cohort exit criteria.
        """
        return [f"Exit Cohort based on the following criteria:"]


# CensoringEvents with ConceptSet
@dataclass
class CensoringEventNormal(CensoringEvent):
    """
    Represents a censoring event that may be associated with a ConceptSet.

    This subclass of CensoringEvent allows linking a ConceptSet to the event,
    enabling more specific cohort exit criteria.

    Attributes
    ----------
    concept_set: ConceptSet, optional
        ConceptSet associated with the censoring event.
        Default is None
    concept_set_name: str, Optional
        Name of the associated ConceptSet, populated automatically if concept_set is provided.
        Default is None

    Methods
    -------
    describe() -> List[str]
        Returns a human-readable description of the censoring event including
        its ConceptSet if available.
    
    Notes
    -----
    This class inherits from CensoringEvent.
    """
    concept_set : Optional[ConceptSet] = None
    concept_set_name : Optional[str] = field(init=False, default=None)

    def __post_init__(self):
        """
        Initializes `concept_set_name` based on `concept_set` after dataclass init.
        """
        if isinstance(self.concept_set, ConceptSet):
            self.concept_set_name = self.concept_set.get_concept_set_name()
        else:
            self.concept_set_name = None

    
    def describe(self) -> List[str]:
        """
        Generates a textual description of the censoring event.

        Returns
        -------
        List[str]
            List containing a single string describing the event,
            including its ConceptSet if available.
        """
        article = self.article()
        return [f"{article} {self.event_type} of {self.concept_set_name}"]



# CensoringEvents without ConceptSet (Payer Period Plan)
@dataclass
class SpecialCensoringEvent(CensoringEvent):
    """
    Represents a censoring event that cannot be associated with a ConceptSet.
    This type has no extra attributes beyond those inherited from CensoringEvent.

    Methods
    -------
    describe() -> List[str]
        Returns a human-readable description of the censoring event
    
    Notes
    -----
    This class inherits from CensoringEvent.
    """

    def describe(self) -> List[str]:
        """
        Generates a textual description of the censoring event.

        Returns
        -------
        List[str]
            List containing a single string describing the event.
        """
        article = self.article()
        return [f"{article} {self.event_type}"]



"""
Subclasses of CensoringEvent representing specific cohort exit events.
- Normal events can have an associated ConceptSet.
- Special events do not have an associated ConceptSet (e.g., PayerPlanPeriodExit).

Notes
------
Each subclass specifies its 'event_type' in the constructor.
The method 'add_attribute()' is a placeholder for adding extra attributes if needed.
All these subclasses inherit from CensoringEventNormal or SpecialCensoringEvent.

Typical usage
-------------
Two specific examples on how to use both types of CensoringEvent with subclasses.

from pysynthea.concept_set.concept_class import ConceptSet
from pysynthea.setup.setup import connect_db
from censoring_events import ConditionEraExit, PayerPlanPeriodExit

1. CensoringEventNormal
    conn = connect_db()
    cs_diabetes = ConceptSet(
        conn=conn, 
        conceptset_name="Diabetes Mellitus",
        concept_ids=[201820, 201826],
        concept_names=["Diabetes mellitus"],
        include_descendants=True
    )
    condition_exit = ConditionEraExit(concept_set=cs_diabetes)
    print(condition_exit.describe())


2. SpecialCensoringEvent
    payer_exit = PayerPlanPeriodExit()
    print(payer_exit.describe())
"""
# add_attribute will be completed to add extra attributes to each event. Repetition is due to changes in these attributes depending on the type of CensoringEvents.

@dataclass
class ConditionEraExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'condition era' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="condition era", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class ConditionOccurrenceExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'condition occurrence' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="condition occurrence", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class DeathExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'death occurrence' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="death occurrence", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class DeviceExposureExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'device exposure' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="device exposure", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class DoseEraExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'dose era' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="dose era", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class DrugEraExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'drug era' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="drug era", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class DrugExposureExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'drug exposure' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="drug exposure", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class MeasurementExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'measurement' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="measurement", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class ObservationExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'observation' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="observation", concept_set=concept_set)

    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class PayerPlanPeriodExit(SpecialCensoringEvent):
    def __init__(self):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'payer plan period' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="payer plan period")

    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class ProcedureOccurrenceExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'procedure occurrence' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="procedure occurrence", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class SpecimenExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'specimen' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="specimen", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class VisitOccurrenceExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'visit occurrence' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="visit occurrence", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class VisitDetailExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'visit detail' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="visit detail", concept_set=concept_set)


    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass
