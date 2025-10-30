from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Literal
from pysynthea.cohort.censoring_events import CensoringEvent

class EventPersistence(Enum):
    END_OF_CONTINUOUS_OBSERVATION = "end_of_continuous_observation" # Sin atributos extra
    FIXED_DURATION = "fixed_duration_relative_to_initial_event"
    END_OF_DRUG_EXPOSURE = "end_of_continuous_drug_exposure"

# Si EventPersistence es FIXED_DURATION
Offset_From = Literal["start date", "end date"]
OffsetDays = Literal[0,1,7,14,21,30,60,90,120,180,365,548,730,1095]

# Si EventPersistence es END_OF_DRUG_EXPOSURE
Window = Literal[0,1,7,14,21,30,60,90,120,180,365,548,730,1095]

@dataclass
class CohortExitEvent:
    event_type: str
    event_persistence: EventPersistence
    censoring_events: Optional[List[CensoringEvent]] = None

    # FIXED_DURATION
    offset_from: Optional[Offset_From] = None
    offset_days: Optional[OffsetDays] = None

    # END_OF_DRUG_EXPOSURE
    drug_concept_set: Optional[str] = None
    surveillance_window: Optional[Window] = None 
    persistence_window: Optional[Window] = None

    force_duration: Optional[bool] = None  # True = usar forced_drug_exposure_window, False = usar days_supply
    drug_exposure_window: Optional[Window] = None  # Solo se usa si force_duration=True. Indica número de días forzados.

    def __post_init__(self):
        # FIXED_DURATION
        if self.event_persistence == EventPersistence.FIXED_DURATION:
            if self.offset_from is None or self.offset_days is None:
                raise ValueError("Para FIXED_DURATION debes indicar offset_from y offset_days")
        else:
            if self.offset_from is not None or self.offset_days is not None:
                raise ValueError("offset_from y offset_days solo se usan con FIXED_DURATION")

        # END_OF_DRUG_EXPOSURE
        if self.event_persistence == EventPersistence.END_OF_DRUG_EXPOSURE:
            if self.drug_concept_set is None:
                raise ValueError("Para END_OF_DRUG_EXPOSURE debes indicar drug_concept_set")
            if self.surveillance_window is None or self.persistence_window is None:
                raise ValueError("Para END_OF_DRUG_EXPOSURE debes indicar surveillance_window y persistence_window")
            if self.force_duration is None:
                raise ValueError("Para END_OF_DRUG_EXPOSURE debes indicar force_duration")
            if self.force_duration and self.drug_exposure_window is None:
                raise ValueError("Si force_duration=True, debes indicar drug_exposure_window")
        else:
            # Evitar usar atributos de END_OF_DRUG_EXPOSURE en otro tipo de evento
            if any([self.drug_concept_set, self.surveillance_window, self.persistence_window,
                    self.force_duration, self.drug_exposure_window]):
                raise ValueError("Atributos de END_OF_DRUG_EXPOSURE solo se usan con ese event_persistence")
