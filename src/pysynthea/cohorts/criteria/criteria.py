from dataclasses import dataclass

from .fathers_criteria import *
from .subgroup_criteria import *
from pysynthea.concept_set.concept_set import *


"""
Criterias
"""
@dataclass
class Add_Condition_Era(Options_Concept):
    criteria_name : str = "condition era"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Condition_Occurrence(Options_Concept_Extra):
    criteria_name : str = "condition occurrence"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Death(Options_Concept):
    criteria_name : str = "death occurrence"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Device_Exposure(Options_Concept_Extra):
    criteria_name : str = "device exposure"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)
    

@dataclass
class Add_Dose_Era(Options_Concept):
    criteria_name : str = "dose era"    
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)
    

@dataclass
class Add_Drug_Era(Options_Concept):
    criteria_name : str = "drug era"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Drug_Exposure(Options_Concept_Extra):
    criteria_name : str = "drug exposure"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Location_Region(Options_Concept):
    criteria_name : str = "location region"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Measurement(Options_Concept_Extra):
    criteria_name : str = "measurement"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Observation(Options_Concept_Extra):
    criteria_name : str = "observation"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"an {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Observation_Period(Options_Extra):
    criteria_name : str = "observation periods"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"{self.criteria_name} with the following criteria: ")
        return "\n".join(list_desc)


@dataclass
class Add_Payer_Plan_Period(Options_Extra):
    criteria_name : str = "payer plan period"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"{self.criteria_name} with the following criteria: " )
        return "\n".join(list_desc)


@dataclass
class Add_Procedure_Occurrence(Options_Concept_Extra):
    criteria_name : str = "procedure occurrence"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Specimen(Options_Concept):
    criteria_name : str = "specimen"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Visit_Occurrence(Options_Concept_Extra):
    criteria_name : str = "visit occurrence"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Visit_Detail(Options_Concept_Extra):
    criteria_name : str = "visit detail"
    def describe(self):
        list_desc = super().describe()
        list_desc.insert(1, f"a {self.criteria_name} of {self.concept_set_name}")
        return "\n".join(list_desc)


@dataclass
class Add_Group(Subgroup_Criteria):
    pass