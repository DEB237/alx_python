"""
This script lists all states with names starting
with 'N' from a MySQL database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=mysql_user,
                         passwd=mysql_password, db=db_name, port=3306)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select states starting with 'N'
    cursor.execute("""SELECT * FROM states WHERE name
                       LIKE BINARY 'N%' ORDER BY states.id""")
 
    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
