from dataclasses import dataclass
from typing import Optional
import pandas as pd


# -----------------------------------------------------------
# CLASE BASE
# -----------------------------------------------------------

@dataclass
class CensoringEvent:
    event_type: str

    def get_event_type(self) -> str:
        return self.event_type


# -----------------------------------------------------------
# CLASES HIJAS
# el método add_attribute se puede completar para añadir a cada tipo de censoring event atributos extras. 
#   Está repetido porque los atributos cambian para cada tipo de CensoringEvent.
# -----------------------------------------------------------

@dataclass
class ConditionEraExit(CensoringEvent):
    condition_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "condition_era"

    def add_attribute(self):
        pass


@dataclass
class ConditionOccurrenceExit(CensoringEvent):
    condition_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "condition_occurrence"

    def add_attribute(self):
        pass


@dataclass
class DeathExit(CensoringEvent):
    death_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "death"

    def add_attribute(self):
        pass


@dataclass
class DeviceExposureExit(CensoringEvent):
    device_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "device_exposure"

    def add_attribute(self):
        pass


@dataclass
class DoseEraExit(CensoringEvent):
    drug_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "dose_era"

    def add_attribute(self):
        pass


@dataclass
class DrugEraExit(CensoringEvent):
    drug_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "drug_era"

    def add_attribute(self):
        pass


@dataclass
class DrugExposureExit(CensoringEvent):
    drug_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "drug_exposure"

    def add_attribute(self):
        pass


@dataclass
class MeasurementExit(CensoringEvent):
    measurement_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "measurement"

    def add_attribute(self):
        pass


@dataclass
class ObservationExit(CensoringEvent):
    observation_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "observation"

    def add_attribute(self):
        pass


@dataclass
class PayerPlanPeriodExit(CensoringEvent):
    event_type: str = "payer_plan_period"

    def add_attribute(self):
        pass


@dataclass
class ProcedureOccurrenceExit(CensoringEvent):
    procedure_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "procedure_occurrence"

    def add_attribute(self):
        pass


@dataclass
class SpecimenExit(CensoringEvent):
    specimen_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "specimen"

    def add_attribute(self):
        pass


@dataclass
class VisitOccurrenceExit(CensoringEvent):
    visit_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "visit_occurrence"

    def add_attribute(self):
        pass


@dataclass
class VisitDetailExit(CensoringEvent):
    visit_detail_concept_set: Optional[pd.DataFrame] = None
    event_type: str = "visit_detail"

    def add_attribute(self):
        pass
