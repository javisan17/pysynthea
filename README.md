# Synthea OMOP Example Database

This project provides a package to work with an **example OMOP database** and run queries and experiments without using real patient data.

## Usage

```python
import pysynthea.build as pb
import sqlalchemy as sa

# Create database
pb.setup_db()

# Connect db
conn = pb.connect_db()

# Queries
cur = conn.execute(sa.text("select count(*) from person"))
cur.fetchone()

# Close conexion
conn.close()
```

## Purpose

This package allows researchers, developers, and students to:

- Learn and practice **SQL queries on the OMOP model**.
- Test health data analysis scripts **without sensitive real data**.
- Have a reproducible environment for **educational and demo purposes**.
