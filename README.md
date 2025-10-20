# Synthea OMOP Example Database

This project provides a package to work with an **example OMOP database** and run queries and experiments without using real patient data.

## Database and usage

The project already includes a **pre-built DuckDB database** ready to use.  
This database contains the complete processed data, allowing you to run queries directly without any additional setup.

In addition, the project provides a **feature to generate a smaller version** of the database.  
This is useful for testing or if you want to **replace the main database**.

### WARNING WITH QUERIES

No database creates schemas, index or relationships between tables. **The Atlas queries do not work**. You need to change it.

### Available options

- **Full database**  
  Already generated and located in the `src/pysynthea/data/` directory.

  ```python
  import pysynthea.build as pb
  import sqlalchemy as sa

  # Connect db. You don't need to specify the database
  conn = pb.connect_db()

  # Queries
  cur = conn.execute(sa.text("select count(*) from person"))
  cur.fetchone()

  # Close conexion
  conn.close()
  ```

- **Generate a smaller database**
  You can create a lightweight version by running:

  ```python
  import pysynthea.build as pb
  import sqlalchemy as sa

  # Create smaller database
  pb.setup_db()

  # Connect db
  conn = pb.connect_db(database="small")

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
