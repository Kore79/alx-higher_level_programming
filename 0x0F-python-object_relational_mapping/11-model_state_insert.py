#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, database):
    """
    Connects to the MySQL database and adds the State object "Louisiana".

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

        # Create State object
        new_state = State(name="Louisiana")

        # Add State object to the session
        session.add(new_state)

        # Commit the session to the database
        session.commit()

        # Print the new states.id
        print(new_state.id)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close session
        session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./add_state.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    add_state(username, password, database)
