#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, database):
    """
    Connects to the MySQL database and changes the name of a State object with id=2 to "New Mexico".

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    try:
        # Create engine
        engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query State object by id
        state_to_change = session.query(State).filter_by(id=2).first()

        # Change name to "New Mexico" if state exists
        if state_to_change:
            state_to_change.name = "New Mexico"
            session.commit()
            print("Name changed successfully")
        else:
            print("State with id=2 not found")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close session
        session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./change_state_name.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    change_state_name(username, password, database)
