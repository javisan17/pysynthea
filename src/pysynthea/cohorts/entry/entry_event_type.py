from dataclasses import dataclass, field
from typing import List, Optional
from pysynthea.concept_set.concept_class import*


"""
Module: entry_event_type

Defines classes representing types of cohort entry events in ATLAS.

There are two main types of entry events:
1. Normal events that can have an associated ConceptSet.
2. Special events that do not have a ConceptSet (e.g., payer plan period and observation period).

The module provides:
- Base classes: EntryEvent, NormalEntryEvent, SpecialEntryEvent
- Subclasses for each event type (ConditionEraEntry, DrugExposureEntry, DeathEntry, etc.)
- Methods for describing events in human-readable form.

Classes
-------
EntryEvent
NormalEntryEvent and SpecialEntryEvent
All their specific subclasses (ConditionEraEntry, ConditionOccurrenceEntry)

Dependencies
-------
concept_class.py
"""

@dataclass
class EntryEvent:
    """
    Base class for events that may cause an entry to a cohort. There are two types of entry events, represented by subclasses.

    Attributes
    ----------
    event_type: str
        Type of entry event.

    Methods
    -------
    article() -> str
        Returns the appropriate English article ("a" or "an") based on the event_type.
        It is later used in the describe() method.
    describe() -> List[str]
        Returns a textual description of the entry event.
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
        Returns a basic description for a cohort entry event.

        Returns
        -------
        List[str]
            A single-element list containing a string describing the cohort exit criteria.
        """
        article = self.article()

        # Avoids AttributeErros by checking if it exists.
        if hasattr(self, "concept_set") and getattr(self, "concept_set", None):
            return [f"{article} {self.event_type} of: {self.concept_set_name}."]
        else:
            return [f"{article} {self.event_type}."]


# EntryEvent with ConceptSet
@dataclass
class NormalEntryEvent(EntryEvent):
    """
    Represents an entry event that may be associated with a ConceptSet.

    This subclass of EntryEvent allows linking a ConceptSet to the event,
    enabling more specific cohort entry criteria.

    Attributes
    ----------
    concept_set: ConceptSet, optional
        ConceptSet associated with the entry event.
        Default is None.
    concept_set_name: str, Optional
        Name of the associated ConceptSet, populated automatically if concept_set is provided.
        Default is None.
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


# EntryEvent without ConceptSet (PayerPlanPeriod and ObservationPeriod)
@dataclass
class SpecialEntryEvent(EntryEvent):
    """
    Represents an entry event that cannot be associated with a ConceptSet.
    This type has no extra attributes beyond those inherited from EntryEvent.
    """
    pass


"""
Subclasses of EntryEvent representing specific cohort entry events.
- Normal events can have an associated ConceptSet.
- Special events do not have an associated ConceptSet (e.g., PayerPlanPeriodExit and ObservationPeriod).

Notes
-----
Each subclass specifies its 'event_type' in the constructor.
The method 'add_attribute()' is a placeholder for adding extra attributes if needed.
All these subclasses inherit from NormalEntryEvent or SpecialEntryEvent.

Typical usage
-------------
Two specific examples on how to use both types of EntryEvent with subclasses.

from pysynthea.concept_set.concept_class import ConceptSet
rom entry_event import ConditionEraEntry, PayerPlanPeriodEntry

1. NormalEntryEvent
    cs_diabetes = ConceptSet(
        conn=None,  # Database connection, replace with actual connection
        conceptset_name="Diabetes Mellitus",
        concept_ids=[201820, 201826],
        concept_names=["Diabetes mellitus"],
        include_descendants=True
    )
    condition_entry = ConditionEraEntry(concept_set=cs_diabetes)
    print(condition_entry.describe())


2. SpecialEntryEvent
    payer_entry = PayerPlanPeriodEntry()
    print(payer_entry.describe())
"""
# add_attribute will be completed to add extra attributes to each event. Repetition is due to changes in these attributes depending on the type of EntryEvent


@dataclass
class ConditionEraEntry(NormalEntryEvent):
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
class ConditionOccurrenceEntry(NormalEntryEvent):
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
class DeathEntry(NormalEntryEvent):
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
class DeviceExposureEntry(NormalEntryEvent):
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
class DoseEraEntry(NormalEntryEvent):
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
class DrugEraEntry(NormalEntryEvent):
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
class DrugExposureEntry(NormalEntryEvent):
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
class MeasurementEntry(NormalEntryEvent):
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
class ObservationEntry(NormalEntryEvent):
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
class ObservationPeriodEntry(SpecialEntryEvent):
    def __init__(self, concept_set=None):
        """
        Parameters
        ----------
        concept_set : ConceptSet, optional
            Optional ConceptSet associated with this event. Defaults to None.

        Notes
        -----
        Initializes `event_type` as 'observation period' and passes `concept_set` to the parent class.
        """
        super().__init__(event_type="observation period")

    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


@dataclass
class PayerPlanPeriodEntry(SpecialEntryEvent):
    def __init__(self, concept_set=None):
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
class ProcedureOccurrenceEntry(NormalEntryEvent):
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
class SpecimenEntry(NormalEntryEvent):
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
class VisitOccurrenceEntry(NormalEntryEvent):
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
class VisitDetailEntry(NormalEntryEvent):
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


