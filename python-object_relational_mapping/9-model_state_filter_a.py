"""
This script that lists all State objects that contain the letter a 
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    engine = create_engine
    (f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all the State objects that contain 'a' and display them
    states=session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()