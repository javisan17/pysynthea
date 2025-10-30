from dataclasses import dataclass
import pandas as pd
from typing import Optional
from pysynthea.cohort.cohort_entry_event import CohortEntryEvent

# -----------------------------------------------------------
# CLASES HIJAS
# el método add_attribute se puede completar para añadir a cada tipo de entry event atributos extras. 
#   Está repetido porque los atributos cambian para cada tipo de CohortEntryEvent.
# -----------------------------------------------------------

@dataclass
class ConditionEraEntry(CohortEntryEvent):
    condition_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "condition_era"

    def add_attribute(self):
        pass


@dataclass
class ConditionOccurrenceEntry(CohortEntryEvent):
    condition_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "condition_occurrence"

    def add_attribute(self):
        pass


@dataclass
class DeathEntry(CohortEntryEvent):
    death_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "death"

    def add_attribute(self):
        pass


@dataclass
class DeviceExposureEntry(CohortEntryEvent):
    device_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "device_exposure"

    def add_attribute(self):
        pass


@dataclass
class DoseEraEntry(CohortEntryEvent):
    drug_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "dose_era"

    def add_attribute(self):
        pass


@dataclass
class DrugEraEntry(CohortEntryEvent):
    drug_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "drug_era"

    def add_attribute(self):
        pass


@dataclass
class DrugExposureEntry(CohortEntryEvent):
    drug_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "drug_exposure"

    def add_attribute(self):
        pass


@dataclass
class MeasurementEntry(CohortEntryEvent):
    measurement_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "measurement"

    def add_attribute(self):
        pass


@dataclass
class ObservationEntry(CohortEntryEvent):
    observation_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "observation"

    def add_attribute(self):
        pass


@dataclass
class ObservationPeriodEntry(CohortEntryEvent):
    event_type: str = "observation_period"

    def add_attribute(self):
        pass


@dataclass
class PayerPlanPeriodEntry(CohortEntryEvent):
    event_type: str = "payer_plan_period"

    def add_attribute(self):
        pass


@dataclass
class ProcedureOccurrenceEntry(CohortEntryEvent):
    procedure_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "procedure_occurrence"

    def add_attribute(self):
        pass


@dataclass
class SpecimenEntry(CohortEntryEvent):
    specimen_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "specimen"

    def add_attribute(self):
        pass


@dataclass
class VisitOccurrenceEntry(CohortEntryEvent):
    visit_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "visit_occurrence"

    def add_attribute(self):
        pass


@dataclass
class VisitDetailEntry(CohortEntryEvent):
    visit_detail_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "visit_detail"

    def add_attribute(self):
        pass


