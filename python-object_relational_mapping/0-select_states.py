"""
This script lists all states from a MySQL database.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(user=mysql_user, passwd=mysql_password,
                         db=db_name, host="localhost", port=3306)
    
    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select all states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()