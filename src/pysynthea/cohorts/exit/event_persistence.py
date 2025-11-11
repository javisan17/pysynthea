from dataclasses import dataclass
from typing import List, Literal, Optional
from pysynthea.concept_set.concept_class import*

"""EventPersistence is part of CohortExitEvent"""

@dataclass
class EventPersistence:

    def persistence_type(self) -> str:
        """type of persistence is indicated"""
        return

    def describe(self) -> List[str]:
        event_desc = [f"Event will persist until: {self.persistence_type()}"]
        return event_desc

"""3 EventPersistence subclasses, each with its own attributes."""

Window = Literal[0,1,7,14,21,30,60,90,120,180,365,548,730,1095]

@dataclass
class EndOfContinuousObservation(EventPersistence):
    """no extras"""
    def persistence_type(self) -> str:
        return "end of continuous observation"

@dataclass
class FixedDuration(EventPersistence):
    offset_from: Literal["start date", "end date"] = "start date"
    offset_days : Window = 0

    def persistence_type(self) -> str:
        return "fixed duration relative to initial event"
    
    def describe(self) -> List[str]:
        event_desc = super().describe()
        event_desc.append(f"Offset from: {self.offset_from}" )
        event_desc.append(f"Number of days offset: {self.offset_days} days")
        return event_desc

@dataclass
class EndOfDrugExposure(EventPersistence):
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
        return "end of a continuous drug exposure"
    
    def describe(self):
        event_desc= super().describe()
        event_desc.append(f"Concept set containing the drug(s) of interest: {self.drug_concept_set_name}")
        event_desc.append(f"Persistence window: allow for a maximum of {self.persistence_window} days between exposure records when inferring the era of persistence exposure")
        event_desc.append(f"Surveillance window: add {self.surveillance_window} days to the end of the era of persistence exposure as an additional period of surveillance prior to cohort exit.")
        if self.force_duration:
            event_desc.append(f"Force drug exposure days supply to: {self.drug_exposure_window} days.") 
        elif self.force_duration is False:
            event_desc.append(f"Use days supply and exposure end date for exposure duration.")
        
        return event_desc