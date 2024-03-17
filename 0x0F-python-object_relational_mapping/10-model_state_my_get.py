#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_state_by_name(username, password, database, state_name):
    """
    Connects to the MySQL database and prints the State object with the specified name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """
    try:
        # Create engine
        engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query State object by name
        state = session.query(State).filter_by(name=state_name).first()

        # Print result
        if state:
            print(state.id)
        else:
            print("Not found")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close session
        session.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./print_state_by_name.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    print_state_by_name(username, password, database, state_name)
