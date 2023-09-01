"""
This script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, 
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Prepare the SQL query to select all cities of the given state
    query = """SELECT cities.name FROM cities JOIN states 
            ON cities.state_id = states.id 
            WHERE states.name = %s ORDER BY cities.id ASC"""
    data = (state_name,)

    # Execute the query
    cursor.execute(query, data)

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    cities_str = ', '.join(cities)
    print(cities_str)

    # Close the database connection
    cursor.close()
    db.close()
    