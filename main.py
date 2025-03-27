# imports
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.exc import IntegrityError


# create your Database
username = "postgres"
password = 1234
host = "localhost"
port = 5432
database = "sqlalchemy2"

connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string,echo=False)
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()


# Defines Models: Users/ Tasks
class User(Base):
    __tablename__ = "users"
    id = Column()
    name = Column()
    email = Column()
    tasks= Column()