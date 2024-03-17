#!/usr/bin/python3
"""
This script takes the name of a state as an argument and lists all cities of that state
from the database hbtn_0e_4_usa (SQL injection free!).
"""

import sys
import MySQLdb

def list_cities_by_state(username, password, database, state_name):
    """
    Connects to the MySQL database and lists all cities of the specified state
    in ascending order by cities.id.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state.

    Returns:
        None
    """
    try:
        # Connect to the database
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = conn.cursor()

        # Execute query using parameterized query to prevent SQL injection
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id = states.id WHERE states.name = %s \
                 ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))

        # Fetch results
        results = cursor.fetchall()

        # Print results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./list_cities_by_state.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_cities_by_state(username, password, database, state_name)
