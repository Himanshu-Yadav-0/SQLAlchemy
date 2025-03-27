from sqlalchemy import create_engine, MetaData,Table,Column,INTEGER,VARCHAR

username = "postgres"
password = 1234
host = "localhost"
port = 5432
database = "sqlalchemy"

connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(connection_string, echo=True)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column('id',INTEGER,primary_key=True),
    Column('name',VARCHAR, nullable=False),
    Column('age',INTEGER)
)
meta.create_all(engine)