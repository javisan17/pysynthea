from dataclasses import dataclass
from typing import Literal, Optional
#from pysynthea.cohort.criteria import Group_Inclusion_Criteria


Window = Literal[0,1,7,14,21,30,60,90,120,180,365,548,730,1095]
LimitEvent = Literal ["all events", "earliest event", "latest event"]

@dataclass
class CohortEntryEvent:
    event_type : str

    # Configuración CohortEntryEvent
        # Valores puestos por defecto pero se pueden cambiar
    limit_initial_events_per_person: LimitEvent = "all events"
    continuous_obs_before: Window = 0
    continuous_obs_after: Window = 0

    # Configuración si se habilitan Restrict initial events
    restrict_initial: bool = False
    restriction_limit_event: Optional[LimitEvent] = None
    restriction_obs_before : Optional[Window] = None
    restriction_obs_after : Optional[Window] = None
    #criterions: Optional[List[Group_Inclusion_Criteria]] = None 

    def __post_init__(self):
        if self.restrict_initial:
            # Inicializar valores por defecto si no se pasan
            if self.restriction_limit_event is None:
                self.restriction_limit_event = "all events"
            if self.restriction_obs_before is None:
                self.restriction_obs_before = 0
            if self.restriction_obs_after is None:
                self.restriction_obs_after = 0
            if self.criterions is None:
                self.criterions = []
        else:
        # Limpiar si restrict_initial=False
            self.restriction_limit_event = None
            self.restriction_obs_before = None
            self.restriction_obs_after = None
            self.criterions = None


    """
    # Añadir criterios a la lista criterions solo si restrict_initial está a True
    def add_criterion(self, criterion: Group_Inclusion_Criteria):
        if not self.restrict_initial:
            raise ValueError("Para añadir criterios restrict_initial debe ser True")
        self.criterions.append(criterion)

    """
