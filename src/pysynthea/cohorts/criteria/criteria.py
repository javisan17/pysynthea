from dataclasses import dataclass
from .fathers_criteria import *
from .subgroup_criteria import *
from pysynthea.concept_set.concept_class import *


"""
Module: criteria

This module contains the different types of criteria. 
Each one of them is represented by a class that includes an attribute and a method.
Three types of criteria are defined, Options_Concept, Options_Extra and Options_Concept_Extra. 
Each one of them specifies their name in the `criteria_name` attribute.

Attributes
----------
criteria_name: str
    specific name of each criterion type.

Methods
-------
describe() -> str
    Returns a human-readable multiline string describing
    each criterion, including its concept set name.

Dependencies
------------
Options_Extra
    Criteria that include an Options object and a 
    restrict_to_the_same_visit_occurrence attribute.
Options_Concept
    Criteria that include a ConceptSet and an Options concept.
Options_Concepts_Extra
    Criteria that include a ConceptSet and an Options object,
    as well as a restrict_to_the_same_visit_occurrence attribute.

Typical usage
-------------
Below are minimal examples of how to instantiate and describe each
main criterion type: Options_Concept, Options_Extra and Options_Concept_Extra.


1. Options_Concept
    from pysynthea.concept_set.concept_set import ConceptSet
    from synthea.setup.setup import connect_db()
    from criteria import Add_Condition_Era

    conn = connect_db()
    cs = ConceptSet(
        conn=conn,
        conceptset_name="Diabetes",
        concept_ids=[201826],
        include_descendants=True)
    cs.build()
    crit = Add_Condition_Era(concept_set=cs)

2. Options_Extra
    from criteria import Add_Observation_Period
    crit = Add_Observation_Period(restrict_to_the_same_visit_occurrence=True)

3. Options_Concept_Extra
    from pysynthea.concept_set.concept_set import ConceptSet
    from synthea.setup.setup import connect_db() 
    from criteria import Add_Drug_Exposure
    
    conn = connect_db()
    antibiotics = ConceptSet(
        conn=conn,
        conceptset_name="Antibiotics",
        concept_names=["Amoxicillin"])
    antibiotics.build()
    crit = Add_Drug_Exposure(concept_set=antibiotics)
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