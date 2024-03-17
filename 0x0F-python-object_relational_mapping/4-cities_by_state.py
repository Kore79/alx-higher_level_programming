#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

def list_cities(username, password, database):
    """
    Connects to the MySQL database and lists all cities in ascending order by cities.id.

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
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
        cursor.execute(query)

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
        print("Usage: ./list_cities.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database)
