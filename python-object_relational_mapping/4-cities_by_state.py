"""
This script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Prepare the SQL query to select all cities
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()