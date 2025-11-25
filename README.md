# Synthea OMOP Example Database

This project provides a package to work with an **example OMOP database** generated using Synthea.

It allows you to run queries and experiments on a realistic data model **without using real patient data**.

## OMOP Database

The project provides two databases:

- **Prebuild full OMOP database** (from Zenodo).

  You can automatically download and import it by running:

  ```python
  from pysynthea.setup.setup import *

  # Download full database
  setup_db()
  ```

- **Generate a smaller database**

  You can create a lightweight version by running:

  ```python
  from pysynthea.setup.setup import *

  # Create smaller database
  setup_db(database="small")
  ```

## Connecting and running SQL queries

Example of use:

```python
from pysynthea.setup.setup import *
import sqlalchemy as sa

# Connect to the full database
conn = connect_db()

# Simple query
result = conn.execute(sa.text("SELECT COUNT(*) FROM person"))
print(result.fetchone())

conn.close()
```

To work with the reduced database:

```python
conn = connect_db(database="small")
```

### WARNING WITH QUERIES

You need to modify the SQL queries because these databases do not use schemas. Make sure the SQL syntax is compatible with DuckDB to avoid execution errors. **The raw Atlas queries do not work. You need to modify them.**

## Modeling ATLAS Concepts

This package includes a **lightweight Object-Oriented representation of the main concepts used by ATLAS cohort definitions**.
This allows users to model Concept Sets, Entry/Exit Events, and Criteria in Python and apply them to the included database.

### Concept Sets

The package provides classes to build OMOP-style Concept Sets, which allow grouping OMOP concepts and their descendants (optional).
These objects mirror the structure of ATLAS Concept Sets and can be attached to criteria and reused across cohorts.

- **Creating a Concept Set**

```python
  from pysynthea.setup.setup import *
  from pysynthea.concept_set import *

  # A connection to a database is required
  conn = connect_db()
  cs = ConceptSet(
      conn=conn,
      conceptset_name="Diabetes Mellitus test",
      concept_ids=[201826, 201820],
      concept_names=["Diabetes mellitus"],
      include_descendants=True
    )

  # Build the final DataFrame that represents the Concept Set
  df = cs.build()
```

### Criteria

Cohort criteria define **additional rules that filter which events or individuals are considered for entry or exit**.

#### Subgroup Criteria

A **subgroup is a collection of criteria** that can be combined using logic such as **all, any, at least, or at most**.

Each subgroup can contain multiple criteria, and a cohort entry/exit event can require a person to satisfy **one or more subgroups**.

#### Named Group Criteria

A named group is a reusable **collection of subgroups**.
Named groups allow you to **organize multiple subgroups under a single label and reuse them across different cohorts**.

#### Inclusion Criteria

Inclusion criteria specify **which named groups must be satisfied for a person to be included in the cohort**.
You can also set whether to consider **all, earliest, or latest events per group**.

- **Creating Criteria**

  ```python
    from pysynthea.cohorts.criteria.criteria import *
    from pysynthea.cohorts.criteria.fathers_criteria import *
    from pysynthea.cohorts.criteria.inclusion_criteria import *
    from pysynthea.cohorts.criteria.group_criteria import *
    from pysynthea.cohorts.criteria.subgroup_criteria import *

  # Criterions (assuming we are reusing the Diabetes ConceptSet and the default parameteres for the Options object)
  opt = Options()
  c1 = Add_Condition_Criteria(concept_set=cs, concept_set_name="Diabetes Mellitus test", options=opt)
  c2 = Add_Observation_Period(options=opts, restrict_to_the_same_visit_occurrence=False)
  c3 = Add_Condition_Occurrence(concept_set=cs, concept_set_name="Diabetes Mellitus test", options= opt, restrict_to_the_same_visit_occurrence= False)
  # Group criterions in subgroups
  group1 = Subgroup_Criteria(having_x_of_the_following_criteria="all", criteria =[c1,c3])
  group2 = Subgroup_Criteria(having_x_of_the_following_criteria="any", criteria=[c2, c3])
  group3 = Subgroup_Criteria(having_x_of_the_following_criteria="all", criteria=[c1, c2])
  # We create Named_Group_Criteria by grouping Subgroup_Criteria
  named_group1 = Named_Group_Criteria(name="Diabetes criteria test", description="A test with criteria involving Diabetes", groups_criteria=[group1, group3])
  named_group2 = named_group1.add_group_criteria(group_criteria=[group2])
  # Finally, we create Inclusion_Criteria by addding the missing attribute
  inclusion1 = Inclusion_Criteria(limit_qualifying_events_to="earliest event", named_criteria=[named_group1, named_group2])
  ```

### Cohort Entry and Exit Events

In ATLAS, cohort entry and exit events define **when a person enters or leaves a cohort**.

#### Cohort Entry Events

Entry events specify the **conditions or occurrences that qualify a person to enter a cohort**.
They can be **combined with Entry Criteria** to restrict by observation windows, number of events, or additional subgroup rules.
In this case, several imports from the Criteria class are required.

- **Defining a Cohort Entry Event**

```python
  from pysynthea.setup.setup import *
  from pysynthea.cohorts.entry.cohort_entry_event import *
  from pysynthea.cohorts.entry.entry_criteria import *
  from pysynthea.cohorts.entry.entry_event_type import *
  from pysynthea.cohorts.criteria.criteria import *
  from pysynthea.cohorts.criteria.subgroup_criteria import *
  from pysynthea.cohorts.criteria.inclusion_criteria import *

  # Connection to a database, the connect_db() method can be found in the setup module..
  conn = connect_db()
  # Needed ConceptSets for some Criteria types
  visit= ConceptSet(conn=conn, conceptset_name="ER visit", concept_names=["Emergency Room Visit"], include_descendants=True)
  procedure= ConceptSet(conn=conn, conceptset_name="C-Section", concept_names="Cesarean section", include_descendants=True)
  # EntryEvent
  entry1=VisitOccurrenceEntry(concept_set=visit)
  entry2=ProcedureOccurrenceEntry(concept_set=procedure)
  # Options object to build conditions (Options_Concept and Options_Concept_Extra)
  opts = Options(
    how_occurrence="at least",
    amount_occurrence=3,
    using_occurrence="using all",
    time_event="event starts",
    time_window_value="all",
    time_window_relation="before",
    reference_window_value=7,
    reference_window_relation="before",
    index_date_point="index end date",
    allow_events_from_outside_observation_period=False)
  # Options_Concept and Options_Concept_Extra
  cond2 = Add_Visit_Occurrence(concept_set=visit, options=opts)
  cond3 = Add_Procedure_Occurrence(concept_set= procedure, options= opts, restrict_to_the_same_visit_occurrence=False)
  # Subgroup_Criteria -> Named_Group_Criteria -> Inclusion_Criteria
  subgr= Subgroup_Criteria(criteria=[cond2, cond3])
  namedgrcrit = Named_Group_Criteria(name="Group 2", description="Patients with an Emergency C-Section", groups_criteria=subgr)
  inccrit=Inclusion_Criteria(named_criteria=namedgrcrit)
  # EntryCriteria
  entrycrit= EntryCriteria(limit_initial_events_per_person="latest event", continuous_obs_before=0, continuous_obs_after= 7, restrict_initial=True, criteria_list_crit=subgr, inclusion_criteria=inccrit)
  # Cohort definition
  cohort= CohortEntryEvent(entry_events=[entry1, entry2], entry_criteria=entrycrit)
  # See results
  print(cohort.describe())
```

#### Cohort Exit Events

Exit events define **conditions for leaving a cohort**, such as the end of drug exposure, death, or specific condition occurrences.
They can also be combined with **event persistence rules** (fixed duration or based on drug exposure) and **censoring events**.

- **Defining a Cohort Exit Event**
  ```python
    from pysynthea.setup.setup import *
    from pysynthea.concept_set.concept_class import*
    from pysynthea.cohorts.exit.event_persistence import *
    from pysynthea.cohorts.exit.cohort_exit_event import *
    from pysynthea.cohorts.exit.censoring_events import *

    # Database connection to build Concept Set.
    conn = connect_db()
    # ConceptSets
    diabetes = ConceptSet(conn=conn, conceptset_name="Diabetes", concept_names=["Diabetes"], include_descendants=True)
    # CensoringEvents
    censoring1 = ConditionEraExit(concept_set=diabetes)
    censoring2 = PayerPlanPeriodExit()
    # EventPersistence
    eventPers = FixedDuration(offset_from='start date', offset_days=30)
    # Cohort definition
    cohort = CohortExitEvent( event_persistence=eventPers, censoring_events=[censoring1, censoring2])
    # See results
    for line in cohort.describe():
      print(line)
  ```

## Testing

Each class has a test to ensure the proper functioning. However, they are intended as standalone integration tests, not unit tests. Every test requires the Synthea database to be available locally.

## Purpose

This package allows researchers, developers, and students to:

- Learn and practice **SQL queries on the OMOP model**.
- Test health data analysis scripts **without sensitive real data**.
- Have a reproducible environment for **educational and demo purposes**.
- **Experiment with ATLAS-like concepts**, such as Concept Sets and Cohorts.