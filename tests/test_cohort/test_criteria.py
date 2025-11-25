"""
TEST criteria. Both ways should return the previously added criterion describe.
Dependencies
------------
criteria.py
fathers_criteria.py
inclusion_criteria.py
group_criteria.py
subgroup_criteria.py
Notes
-----
- Requires the Synthea database to be available locally.
- Intended as a standalone integration test, not a unit test.
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
    # Create class.  Criterions are added after.
    criterias = Inclusion_Criteria()
    # Create criterion.
    criterion1 = Add_Observation_Period()
    print(criterion1.describe())
    # Create groups.
    subgroup = Subgroup_Criteria(criteria=[criterion1])
    group = Named_Group_Criteria(name="test1", description="", groups_criteria=[subgroup])
    criterias.add_named_criteria(group=group)
    for named_criteria in criterias.get_named_criteria():
        for subgroup in named_criteria.get_group_criteria():
            for criteria in subgroup.get_criteria():
                print(criteria.describe())
if __name__ == '__main__':
    main()