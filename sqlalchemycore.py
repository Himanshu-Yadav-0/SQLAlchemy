# Importing necessary modules from SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, INTEGER, VARCHAR

# Step 1: Define Database Credentials
# These are the details to connect to your PostgreSQL database.
username = "postgres"        # Your PostgreSQL username
password = 1234              # Your PostgreSQL password (use secure methods in production)
host = "localhost"           # The host where your database is running (usually localhost)
port = 5432                  # Default PostgreSQL port
database = "sqlalchemy"      # The name of your PostgreSQL database

# Step 2: Create a Connection String
# This string is in the format required by SQLAlchemy to connect to PostgreSQL.
connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"

# Step 3: Create an Engine
# The engine is responsible for managing the connection to the database.
# `echo=True` prints all the generated SQL statements for debugging.
engine = create_engine(connection_string, echo=True)

# Step 4: Initialize Metadata
# Metadata holds information about the database schema (tables, columns, etc.).
meta = MetaData()

# Step 5: Define a Table Schema
# We are defining a table named "people" with 3 columns: id, name, and age.
people = Table(
    "people",               # Table name
    meta,                   # Metadata object (stores schema)
    Column('id', INTEGER, primary_key=True),       # 'id' is the primary key (unique identifier)
    Column('name', VARCHAR, nullable=False),       # 'name' is a string (cannot be null)
    Column('age', INTEGER)                         # 'age' is an integer (can be null)
)

# Step 6: Create the Table in the Database
# If the table doesn't already exist, this will create it.
# meta.create_all(engine)

# Step 7: Establish a Connection
# Connect to the database using the engine.
conn = engine.connect()

# Step 8: Create an Insert Statement
# We are inserting a new record with specific values for id, name, and age.
# insert_statement = people.insert().values(
#     id=2,                  # Setting id to 1
#     name='isha',       # Setting name to "Himanshu"
#     age=21                 # Setting age to 21
# )

# # Step 9: Execute the Insert Query
# # This sends the INSERT statement to the database.
# result = conn.execute(insert_statement)

# # Step 10: Commit the Transaction
# # Commits the changes to make the insert permanent.
# conn.commit()

# (Optional) Close the Connection
# Always close the connection after the operation is complete.

# select_statement = people.select()
update_statement = people.update().where(people.c.id == 1).values(name = 'HY')
conn.execute(update_statement)
# for row in result.fetchall():
#     print(row)
conn.commit()


conn.close()
