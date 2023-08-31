"""
This script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa 
where name matches the argument. But this time, write one that is safe from MySQL injections!
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
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Prepare the SQL query with query parameterization
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    data = (state_name,)

    # Execute the query
    cursor.execute(query, data)

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()