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
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    tasks = relationship("Tasks",back_populates="user",cascade="all,delete-orphan")

class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True)
    title = Column(String[50],nullable=False)
    description = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))
    user = relationship("User",back_populates='tasks')

Base.metadata.create_all(engine)


# Utility Functions

def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()

def confirm_action(prompt:str)->bool:
    return input(f"{prompt} (yes/no):").strip().lower() == 'yes'

# CRUD Ops
def add_user():
    name,email = input("Enter user Name:"), input("Enter teh email:")
    if get_user_by_email(email):
        print(f"User already exists: {email}")
        return
    try:
        session.add(User(name = name,email = email))
        session.commit()  
        print(f"User: {name} is added successfully")
    except IntegrityError:
        session.rollback() 
        print(f"Error")

def add_task():
    email = input("Enter the email of the user to add taskes:")
    user = get_user_by_email(email)
    if not user:
        print(f"No user found with that email!")
        return
    title,description = input("Enter the title: "), input("Enter the description: ")
    session.add(Tasks(title = title, description = description,user= user))
    session.commit()
    print(f"Added to the database: {title}:{description}")

def query_users():
    for user in session.query(User).all():
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

def query_tasks():
    email = input("Enter the email of the user for tasks: ")
    user = get_user_by_email(email)
    if not user:
        print("There was no User with that email")
        return
    for task in user.tasks:
        print(f"Task ID: {task.id}, Title: {task.title}")

# Main Ops

def main() -> None:
    actions = {
        "1":add_user,
        "2":add_task,
        "3":query_users,
        "4":query_tasks
    }
    try:
        while True:
            print ("\nOptions: \nl. Add User\n2. Add Task\n3. Query Users\n4. Query Tasks\n5. Update User\n6. Delete User\n7. Delete Task\n8. Exit")
            choice = input("Enter an option: ")
            if choice == "8":
                print("Bye Bye!!!")
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("That is not an Option")
    except KeyboardInterrupt:
        print("Intruppted By User")

if __name__ == '__main__':
    main()