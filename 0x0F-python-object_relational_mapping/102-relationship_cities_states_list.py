#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City

def list_cities(username, password, database):
    """
    Connects to the MySQL database and lists all City objects
    sorted in ascending order by cities.id.

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

        # Query all City objects
        cities = session.query(City).order_by(City.id).all()

        # Print results
        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close session
        session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./list_cities.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database)
