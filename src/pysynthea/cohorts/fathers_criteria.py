from dataclasses import dataclass, field
from typing import Literal, Optional
import pandas as pd


"""
Clase padre de criterios
"""
@dataclass
class Criteria:
    atributes: list[object] = field(default_factory=list)
    def add_attribute(self):
        pass


"""
2 hijos: demographic (solo atributos) y opciones
"""
@dataclass
class Add_Demographic(Criteria):
    pass

@dataclass
class Options(Criteria):
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

    def describe(self):
        if self.using_occurrence == "using all":
            occurrence_desc = f"with {self.how_occurrence} {self.amount_occurrence} {self.using_occurrence} occurrences of:"
        else:
            occurrence_desc = f"with {self.how_occurrence} {self.amount_occurrence} {self.using_occurrence} {self.choice_using_distinct}:"

        time_desc = (
            f"where {self.time_event} between \n"
            f"{self.time_window_value} days {self.time_window_relation} and "
            f"{self.reference_window_value} days {self.reference_window_relation} {self.index_date_point}"
        )

        outside_obs = ""
        if getattr(self, "allow_events_from_outside_observation_period", False):
            outside_obs = "allow events from outside observation period"

        list_desc = [occurrence_desc, time_desc, outside_obs]
        return list_desc


"""
3 tipos dentro de cosas: cosas+concept, cosas+extra y cosas+concept+extra
"""

@dataclass
class Options_Concept(Options):
    concept_set: pd.DataFrame = None

@dataclass
class Options_Extra(Options):
    restrict_to_the_same_visit_occurrence: Literal[True, False] = False

    def describe(self):
        list_desc = super().describe()

        same_visit = ""
        if getattr(self, "restrict_to_the_same_visit_occurrence", False):
            same_visit = "restrict to the same visit occurrence"

        return list_desc.append(same_visit)

@dataclass
class Options_Concept_Extra(Options):
    concept_set: pd.DataFrame = None
    restrict_to_the_same_visit_occurrence: Literal[True, False] = False

    def describe(self):
        list_desc = super().describe()

        same_visit = ""
        if getattr(self, "restrict_to_the_same_visit_occurrence", False):
            same_visit = "restrict to the same visit occurrence"
            
        return list_desc.append(same_visit)