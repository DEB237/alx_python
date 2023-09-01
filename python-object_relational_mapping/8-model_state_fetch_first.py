"""
This script prints the first State object from 
the database hbtn_0e_6_usa
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

    # Fetch the first State object and display it
    state = session.query(State).order_by(State.id).first()
    if state is not None:
      print(f"{state.id}: {state.name}")
    else:
      print("Nothing")

    # Close the session
    session.close()