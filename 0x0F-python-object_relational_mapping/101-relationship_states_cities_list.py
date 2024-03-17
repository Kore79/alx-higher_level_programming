#!/usr/bin/python3
"""
This script lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State

def list_states_and_cities(username, password, database):
    """
    Connects to the MySQL database and lists all State objects,
    and corresponding City objects, sorted in ascending order by states.id and cities.id.

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

        # Query State objects with their corresponding City objects
        states = session.query(State).order_by(State.id).all()

        # Print results
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close session
        session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./list_states_and_cities.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_and_cities(username, password, database)
