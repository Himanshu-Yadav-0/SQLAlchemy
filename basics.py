from sqlalchemy import create_engine,text
from sqlalchemy.orm import Session

username = "postgres"
password = 1234
host = "localhost"
port = 5432
database = "sqlalchemy"

connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(connection_string, echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS people (name varchar(20), age int);"))

conn.commit()


session = Session(engine)

session.execute(text("INSERT INTO PEOPLE (NAME,AGE) VALUEs ('Himanshu',21);"))

session.commit()