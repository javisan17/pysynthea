from dataclasses import dataclass, field
from typing import List, Literal, Optional
from pysynthea.concept_set.concept_class import*

"""
Module: fathers.criteria

Dependencies
------------
concept_class.py

Classes
-------
Criteria
Add_Demographic
Options
Options_Concept. Options_Extra, Options_Concept_Extra

Typical Usage
-------------
This module defines multiple classes. An example on how to use the `Options_Concept_Extra` criterion is given. It extends
`Criteria` by associating it with a `ConceptSet`, additional counting and 
temporal `Options`, and an optional restriction to the same visit occurrence.

from pysynthea.criteria.options_concept_extra import Options_Concept_Extra
from pysynthea.criteria.base import Criteria
from pysynthea.concept_set.conceptset import ConceptSet
from pysynthea.criteria.options import Options

1. Create or retrieve a ConceptSet
    my_concept_set = ConceptSet(
        name="Diabetes concept set",
        concepts=[201254, 201820])

2. Create Options (optional — defaults are provided)
    opt = Options(
        count="first",
        ignore_observation_period=False,
        restrict_to_first_occurrence=True)

3. Instantiate the criterion with extra concept configuration
    crit = Options_Concept_Extra(
        concept_set=my_concept_set,
        options=opt,
        restrict_to_the_same_visit_occurrence=True)

4. Generate a human-readable description
    description = crit.describe()
    print(description)
"""

@dataclass
class Criteria:
    """
    This class represents a single criteria's structure in ATLAS.

    Attributes
    ----------
    attributes: List[Object]


    Methods
    -------
    describe() -> List[str]
        Returns a human-readable description of the criteria.
    add_attribute()
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
    """
    attributes: list[object] = field(default_factory=list)
    
    def describe(self) -> List[str]:
        """
        Creates an empty list that will be filled by appending the Criteria object description.

        Returns
        -------
        List[str]
            It will store the Criteria object description.
        """
        return []
    
    def add_attribute(self):
        """
        Placeholder for adding extra attributes specific to the subclass.
        To be implemented as needed.
        """
        pass


"""
4 Criteria subclasses
    Add_Demographic (only Add Attributes function, hence it will be later implemented)
    Options_Concept, Options_Extra, Options_Concept_Extra
"""
@dataclass
class Add_Demographic(Criteria):
    """"
    Represents the Add Attribute possibility in ATLAS. 
    To be implemented in the future.
    """
    #def describe(self):
        #return super().describe() --> poner cuando se añadan los atributos
    pass

@dataclass
class Options:
    """
    Represents the setting options applied to a single criterion within a cohort 
    definition.These options determine how occurrences are counted, how time windows
    are applied, and whether events outside the observation period are allowed.

    Attributes
    ----------
    how_occurrence : Literal["at least", "exactly", "at most"]
        Specifies the occurrence constraint applied to the event.
        Default is "at least".
    amount_occurrence: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100]
        Number of occurrences required.
        Default is 1.
    using_occurrence: Literal["using all", "using distinct"]
        Determines whether all occurrences or only distinct ones are counted.
        Default is "using all".
    choice_using_distinct: Literal["Standard Concept", "Start Date"], optional
        When 'using_occurrence="using distinct"', determines the criterion used
        to define distinct occurrences.
        Default is "Standard Concept".
    time_event: Literal["event starts", "event ends"]
        Specifies which time anchor of the event is used for window evaluation.
        Default is "event starts".
    time_window_value: Literal["all", 0, 1, 7, 14, 21, 30, 60, 90, 120, 180, 365, 548, 730, 1095]
         First value of the relative time window.
        Default is "all".
    time_window_relation: Literal["before", "after"]
        Specifies how the time window relates to the event.
        Default is "before".
    reference_window_value: Literal["all", 0, 1, 7, 14, 21, 30, 60, 90, 120, 180, 365, 548, 730, 1095]
        Second value of the relative time window.
        Default is "all".
    reference_window_relation: Literal["before", "after"]
        Specifies how the reference window relates to the index date.
        Default is "after".
    index_date_point: Literal["index start date", "index end date"]
        Defines whether the start or end of the index event is used as reference.
        Default is "index start date".
    allow_events_from_outside_observation_period: Literal[True, False]
        If True, events outside the observation period are included.
        Default is "False".

    Methods
    -------
    describe() -> List[str]
        Returns a list of human-readable sentences describing the configured options.
    """
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
        """
        Generate a human-readable description of the configured options.

        Returns
        -------
        List[str]
            A list of strings, where each string describes one aspect of the
            configuration. 
        """
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


@dataclass
class Options_Concept(Criteria):
    """
    Represents criteria with an associated ConceptSet in ATLAS. It is enriched 
    with additional configuration stored in an Options object.

    Attributes
    ----------
    concept_set : ConceptSet
        ConceptSet associated with this criterion.
        Default is None.
    concept_set_name: str
        Name of the associated ConceptSet.
        Automatically populated, do not assign it manually.
    options: Options
        Represents this specific criterion configuration on how occurrences are counted,
        how temporal constraints are applied, and whether events outside the
        observation period are included.

    Methods
    -------
    describe() -> List[str]
        Returns a human-readable description list summarizing the
        criterion.
    """
    concept_set: ConceptSet = None
    concept_set_name : str = field(init=False, default=None)
    options : Options = field(default_factory=Options)

    def __post_init__(self):
        """
        If there is a concept set, it utomatically populates
        `concept_set_name` based on the provided `concept_set`.

        Notes
        -----
        - Users should not manually assign `concept_set_name`.
        - This method guarantees consistency between the ConceptSet object
          and its registered name.
        """
        if isinstance(self.concept_set, ConceptSet):
            self.concept_set_name = self.concept_set.get_concept_set_name()
        else:
            self.concept_set_name = None
        
    def describe(self)->List[str]:
        """
        Build a combined description of this criterion, including 
        the base description provided by Criteria and the additional 
        description from the Options instance.

        Returns
        -------
        List[str]
            A list of human-readable description strings.
        """
        list_desc = super().describe()
        list_desc.extend(self.options.describe())
        return list_desc

@dataclass
class Options_Extra(Criteria):
    """
    Represents criteria without concept sets in ATLAS.
    An Options object and an additional attribute (restrict_to_the_same_visit_occurrence) are included.

    Attributes
    ----------
    restrict_to_the_same_visit_occurrence : Literal[True, False]
        If True, only events occurring within the same visit occurrence
        are considered valid for this criterion.
        Default is False
    options : Options
        Represents this specific criterion configuration on how occurrences are counted,
        how temporal constraints are applied, and whether events outside the
        observation period are included.

    Methods
    -------
    describe() -> List[str]
        Generates a human-readable list of strings describing the criterion,
        including inherited base description, options configuration, and
        any additional constraints defined in this class.
    """
    restrict_to_the_same_visit_occurrence: Literal[True, False] = False
    options : Options = field(default_factory=Options)

    def describe(self):
        """
        Produce a detailed description of this criterion.

        Returns
        -------
        List[str]
            A list of descriptive strings that includes:
            - The base description provided by the parent 'Criteria' class.
            - The description of the associated 'Options' object.
            - An additional line indicating restriction to the same visit
              occurrence, if enabled.
        """
        list_desc = super().describe()

        list_desc.extend(self.options.describe())

        if getattr(self, "restrict_to_the_same_visit_occurrence", False):
            same_visit = "restrict to the same visit occurrence"
            list_desc.append(same_visit)
        return list_desc

@dataclass
class Options_Concept_Extra(Criteria):
    """
    Attributes
    ----------
    concept_set : ConceptSet
        ConceptSet associated with this criterion.
        Default is None.
    concept_set_name: str
        Name of the associated ConceptSet.
        Automatically populated, do not assign it manually.
    options : Options
        Represents this specific criterion configuration on how occurrences are counted,
        how temporal constraints are applied, and whether events outside the
        observation period are included.
    restrict_to_the_same_visit_occurrence : Literal[True, False]
        If True, only events occurring within the same visit occurrence
        are considered valid for this criterion.
        Default is False

    Methods
    -------
    describe() -> List[str]
        Returns a human-readable description of this criterion, including
        ConceptSet, options, and visit-occurrence restrictions (if any).
    """
    concept_set: ConceptSet = None
    concept_set_name : str = field(init=False, default=None)
    options : Options = field(default_factory=Options)
    restrict_to_the_same_visit_occurrence: Literal[True, False] = False

    def __post_init__(self):
        """
        If there is a concept set, it utomatically populates
        `concept_set_name` based on the provided `concept_set`.

        Notes
        -----
        - Users should not manually assign `concept_set_name`.
        - This method guarantees consistency between the ConceptSet object
          and its registered name.
        """
        if isinstance(self.concept_set, ConceptSet):
            self.concept_set_name = self.concept_set.get_concept_set_name()
        else:
            self.concept_set_name = None

    def describe(self):
        """
        Builds a combined description of this criterion, including the base
        description from Criteria, the Options description, and the optional
        visit-level restriction.

        Returns
        -------
        List[str]
            A list of human-readable description strings.
        """
        list_desc = super().describe()

        list_desc.extend(self.options.describe())

        if getattr(self, "restrict_to_the_same_visit_occurrence", False):
            same_visit = "restrict to the same visit occurrence"
            list_desc.append(same_visit)
        return list_desc