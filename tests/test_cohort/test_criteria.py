"""
TEST criterios. Ambas formas deben devolver lo mismo, el describe del criterio añadido.
"""


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "src"))

from pysynthea.cohorts.criteria.criteria import *
from pysynthea.cohorts.criteria.fathers_criteria import *
from pysynthea.cohorts.criteria.inclusion_criteria import *
from pysynthea.cohorts.criteria.group_criteria import *
from pysynthea.cohorts.criteria.subgroup_criteria import *


def main():
    # Se crea la clase y se van añadiendo criterios
    criterias = Inclusion_Criteria()

    # Se crean los criterios
    criterio1 = Add_Observation_Period()
    print(criterio1.describe())

    #
    subgroup = Subgroup_Criteria(criteria=[criterio1])
    group = Named_Group_Criteria(name="test1", description="", groups_criteria=[subgroup])

    criterias.add_named_criteria(group=group)

    for named_criteria in criterias.get_named_criteria():
        for subgroup in named_criteria.get_group_criteria():
            for criteria in subgroup.get_criteria():
                print(criteria.describe())






if __name__ == '__main__':
    main()