from dataclasses import dataclass, field
from typing import Literal, Optional
import pandas as pd

from .fathers_criteria import *
from subgroup_criteria import *


"""
Criterias
"""
@dataclass
class Add_Condition_Era(Options_Concept):
    def describe(self):
        list_desc = super().describe()
        desc = f"{list_desc[0]}\na condition era of {self.concept_set}\n{list_desc[1]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Condition_Occurrence(Options_Concept_Extra):
    def describe(self):
        list_desc = super().describe()
        desc += f"{list_desc[0]}\na condition occurrence of {self.concept_set}\n{list_desc[1]}\n{list_desc[3]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Death(Options_Concept):
    def describe(self):
        list_desc = super().describe()
        desc = f"{list_desc[0]}\na death occurrence of {self.concept_set}\n{list_desc[1]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Device_Exposure(Options_Concept_Extra):
    def describe(self):
        list_desc = super().describe()
        desc += f"{list_desc[0]}\na device exposure of {self.concept_set}\n{list_desc[1]}\n{list_desc[3]}\n{list_desc[2]}"
        return desc
    

@dataclass
class Add_Dose_Era(Options_Concept):    
    def describe(self):
        list_desc = super().describe()
        desc = f"{list_desc[0]}\na dose era of {self.concept_set}\n{list_desc[1]}\n{list_desc[2]}"
        return desc
    

@dataclass
class Add_Drug_Era(Options_Concept):
    def describe(self):
        list_desc = super().describe()
        desc = f"{list_desc[0]}\na drug era of {self.concept_set}\n{list_desc[1]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Drug_Exposure(Options_Concept_Extra):
    def describe(self):
        list_desc = super().describe()
        desc += f"{list_desc[0]}\na drug exposure of {self.concept_set}\n{list_desc[1]}\n{list_desc[3]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Location_Region(Options_Concept):
    def describe(self):
        list_desc = super().describe()
        desc = f"{list_desc[0]}\na location region of {self.concept_set}\n{list_desc[1]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Measurement(Options_Concept_Extra):
    def describe(self):
        list_desc = super().describe()
        desc += f"{list_desc[0]}\na measurement of {self.concept_set}\n{list_desc[1]}\n{list_desc[3]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Observation(Options_Concept_Extra):
    def describe(self):
        list_desc = super().describe()
        desc += f"{list_desc[0]}\nan observation of {self.concept_set}\n{list_desc[1]}\n{list_desc[3]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Observation_Period(Options):
    def describe(self):
        list_desc = super().describe()
        desc = f"{list_desc[0]}\nobservation periods with the following criteria: \n{list_desc[1]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Payer_Plan_Period(Options_Extra):
    def describe(self):
        list_desc = super().describe()
        desc += f"{list_desc[0]}\nplayer plan period with the following criteria: \n{list_desc[1]}\n{list_desc[3]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Procedure_Occurrence(Options_Concept_Extra):
    def describe(self):
        list_desc = super().describe()
        desc += f"{list_desc[0]}\nan procedure occurrence of {self.concept_set}\n{list_desc[1]}\n{list_desc[3]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Specimen(Options_Concept):
    def describe(self):
        list_desc = super().describe()
        desc = f"{list_desc[0]}\na specimen of {self.concept_set}\n{list_desc[1]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Visit_Occurrence(Options_Concept_Extra):
    def describe(self):
        list_desc = super().describe()
        desc += f"{list_desc[0]}\na visit occurrence of {self.concept_set}\n{list_desc[1]}\n{list_desc[3]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Visit_Detail(Options_Concept_Extra):
    def describe(self):
        list_desc = super().describe()
        desc += f"{list_desc[0]}\na visit detail of {self.concept_set}\n{list_desc[1]}\n{list_desc[3]}\n{list_desc[2]}"
        return desc


@dataclass
class Add_Group(Subgroup_Criteria):
    pass