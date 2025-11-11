from dataclasses import dataclass, field
from typing import List, Optional
from pysynthea.concept_set.concept_class import*


"""Father class for CensoringEvents"""
@dataclass 
class CensoringEvent:
    event_type:str

    def article(self) -> str:
        """Devuelve 'a' o 'an' según la primera letra del evento."""
        return "an" if self.event_type.startswith(("a", "e", "i", "o", "u")) else "a"
    
    def describe(self) -> List[str]:
        return [f"Exit Cohort based on the following criteria:"]


# CensoringEvents with ConceptSet
@dataclass
class CensoringEventNormal(CensoringEvent):
    concept_set : Optional[ConceptSet] = None
    concept_set_name : Optional[str] = field(init=False, default=None)

    def __post_init__(self):
        if isinstance(self.concept_set, ConceptSet):
            self.concept_set_name = self.concept_set.get_concept_set_name()
        else:
            self.concept_set_name = None

    
    def describe(self) -> List[str]:
        article = self.article()
        return [f"{article} {self.event_type} of {self.concept_set_name}"]


# CensoringEvents without ConceptSet (Payer Period Plan)
@dataclass
class SpecialCensoringEvent(CensoringEvent):
    def describe(self) -> List[str]:
        article = self.article()
        return [f"{article} {self.event_type}"]



"""Subclasses"""
# add_attribute will be completed to add extra attributes to each event. Repetition is due to changes in these attributes depending on the type of EntryEvent

@dataclass
class ConditionEraExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="condition era", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class ConditionOccurrenceExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="condition occurrence", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class DeathExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="death occurrence", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class DeviceExposureExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="device exposure", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class DoseEraExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="dose era", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class DrugEraExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="drug era", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class DrugExposureExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="drug exposure", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class MeasurementExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="measurement", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class ObservationExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="observation", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class PayerPlanPeriodExit(SpecialCensoringEvent):
    def __init__(self):
        super().__init__(event_type="payer plan period")

    def add_attribute(self):
        pass


@dataclass
class ProcedureOccurrenceExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="procedure occurrence", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class SpecimenExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="specimen", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class VisitOccurrenceExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="visit occurrence", concept_set=concept_set)


    def add_attribute(self):
        pass


@dataclass
class VisitDetailExit(CensoringEventNormal):
    def __init__(self, concept_set=None):
        super().__init__(event_type="visit detail", concept_set=concept_set)


    def add_attribute(self):
        pass
