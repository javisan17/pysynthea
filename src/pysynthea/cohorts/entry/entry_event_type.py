from dataclasses import dataclass, field
from typing import List, Optional
from pysynthea.concept_set.concept_class import*

"""Father father class"""
@dataclass
class EntryEvent:
    event_type:str

    def article(self) -> str:
        return "an" if self.event_type.startswith(("a", "e", "i", "o", "u")) else "a"
    
    def describe(self) -> List[str]:
        """Devuelve descripción estándar, con o sin concept set."""
        article = self.article()

        # Evita el AttributeError: comprueba si el atributo existe
        if hasattr(self, "concept_set") and getattr(self, "concept_set", None):
            return [f"{article} {self.event_type} of: {self.concept_set_name}."]
        else:
            return [f"{article} {self.event_type}."]


# EntryEvent with ConceptSet
@dataclass
class NormalEntryEvent(EntryEvent):
    concept_set : Optional[ConceptSet] = None
    concept_set_name : Optional[str] = field(init=False, default=None)

    def __post_init__(self):
        if isinstance(self.concept_set, ConceptSet):
            self.concept_set_name = self.concept_set.get_concept_set_name()
        else:
            self.concept_set_name = None


# EntryEvent without ConceptSet (PayerPlanPeriod and ObservationPeriod)
@dataclass
class SpecialEntryEvent(EntryEvent):
    pass


"""Subclasses"""
# add_attribute will be completed to add extra attributes to each event. Repetition is due to changes in these attributes depending on the type of EntryEvent


@dataclass
class ConditionEraEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="condition era", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class ConditionOccurrenceEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="condition occurrence", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class DeathEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="death occurrence", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class DeviceExposureEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="device exposure", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class DoseEraEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="dose era", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class DrugEraEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="drug era", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class DrugExposureEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="drug exposure", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class MeasurementEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="measurement", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class ObservationEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="observation", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class ObservationPeriodEntry(SpecialEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="observation period")

    def add_attribute(self):
        pass


@dataclass
class PayerPlanPeriodEntry(SpecialEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="payer plan period")

    def add_attribute(self):
        pass


@dataclass
class ProcedureOccurrenceEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="procedure occurrence", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class SpecimenEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="specimen", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class VisitOccurrenceEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="visit occurrence", concept_set=concept_set)

    def add_attribute(self):
        pass


@dataclass
class VisitDetailEntry(NormalEntryEvent):
    def __init__(self, concept_set=None):
        super().__init__(event_type="visit detail", concept_set=concept_set)

    def add_attribute(self):
        pass


