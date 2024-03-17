#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

def list_states(username, password, database):
    """
    Connects to the MySQL database and lists all states in ascending order by states.id.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    try:
        # Connect to the database
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = conn.cursor()

        # Execute query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

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
    if len(sys.argv) != 4:
        print("Usage: ./list_states.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)

