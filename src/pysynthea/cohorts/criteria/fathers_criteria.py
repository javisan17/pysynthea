from dataclasses import dataclass, field
from typing import List, Literal, Optional
from pysynthea.concept_set.concept_class import*



"""
Clase padre de criterios
"""
@dataclass
class Criteria:
    atributes: list[object] = field(default_factory=list)
    
    def describe(self) -> List[str]:
        return []
    
    def add_attribute(self):
        pass


"""
2 hijos: demographic (solo atributos) y opciones
"""
@dataclass
class Add_Demographic(Criteria):
    #def describe(self):
        #return super().describe() --> poner cuando se añadan los atributos
    pass

@dataclass
class Options:
    how_occurrence: Literal["at least", "exactly", "at most"] = "at least"
    amount_occurrence: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100] = 1
    using_occurrence: Literal["using all", "using distinct"] = "using all"
    choice_using_distinct: Optional[Literal["Standard Concept", "Start Date"]] = "Standard Concept"
    time_event: Literal["event starts", "event ends"] = "event starts"
    time_window_value: Literal["all", 0, 1, 7, 14, 21, 30, 60, 90, 120, 180, 365, 548, 730, 1095] = "all"
    time_window_relation: Literal["before", "after"] = "before"
    reference_window_value: Literal["all", 0, 1, 7, 14, 21, 30, 60, 90, 120, 180, 365, 548, 730, 1095] = "all"
    reference_window_relation: Literal["before", "after"] = "after"
    index_date_point: Literal["index start date", "index end date"] = "index start date"
    allow_events_from_outside_observation_period: Literal[True, False] = False

    def describe(self) -> List[str]:
        opt_desc=[]
        if self.using_occurrence == "using all":
            opt_desc.append(f"with {self.how_occurrence} {self.amount_occurrence} {self.using_occurrence} occurrences of:")
        else:
            opt_desc.append(f"with {self.how_occurrence} {self.amount_occurrence} {self.using_occurrence} {self.choice_using_distinct}:")

        opt_desc.append(
            f"where {self.time_event} between \n"
            f"{self.time_window_value} days {self.time_window_relation} and "
            f"{self.reference_window_value} days {self.reference_window_relation} {self.index_date_point}"
        )
        if getattr(self, "allow_events_from_outside_observation_period", False):
            opt_desc.append("allow events from outside observation period")
        return opt_desc
        # añadir algo en caso de que allo_events... esté a False?


"""
3 tipos dentro de cosas: cosas+concept, cosas+extra y cosas+concept+extra
"""
# Función para recuperar el nombre de un concept set



@dataclass
class Options_Concept(Criteria):
    concept_set: ConceptSet = None
    concept_set_name : str = field(init=False, default=None)
    options : Options = field(default_factory=Options)

    def __post_init__(self):
        if isinstance(self.concept_set, ConceptSet):
            self.concept_set_name = self.concept_set.get_concept_set_name()
        else:
            self.concept_set_name = None
        
    def describe(self)->List[str]:
        list_desc = super().describe()
        list_desc.extend(self.options.describe())
        return list_desc

@dataclass
class Options_Extra(Criteria):
    restrict_to_the_same_visit_occurrence: Literal[True, False] = False
    options : Options = field(default_factory=Options)

    def describe(self):
        list_desc = super().describe()

        list_desc.extend(self.options.describe())

        if getattr(self, "restrict_to_the_same_visit_occurrence", False):
            same_visit = "restrict to the same visit occurrence"
            list_desc.append(same_visit)
        return list_desc

@dataclass
class Options_Concept_Extra(Criteria):
    concept_set: ConceptSet = None
    concept_set_name : str = field(init=False, default=None)
    options : Options = field(default_factory=Options)
    restrict_to_the_same_visit_occurrence: Literal[True, False] = False

    def __post_init__(self):
        if isinstance(self.concept_set, ConceptSet):
            self.concept_set_name = self.concept_set.get_concept_set_name()
        else:
            self.concept_set_name = None

    def describe(self):
        list_desc = super().describe()

        list_desc.extend(self.options.describe())

        if getattr(self, "restrict_to_the_same_visit_occurrence", False):
            same_visit = "restrict to the same visit occurrence"
            list_desc.append(same_visit)
        return list_desc