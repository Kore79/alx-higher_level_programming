#!/usr/bin/python3
"""
This script takes an argument and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb

def search_states_by_name(username, password, database, state_name):
    """
    Connects to the MySQL database and displays all values in the states table
    where name matches the provided state_name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): The name of the state to search for.

    Returns:
        None
    """
    try:
        # Connect to the database
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = conn.cursor()

        # Execute query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
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
        print("Usage: ./search_states_by_name.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    search_states_by_name(username, password, database, state_name)

