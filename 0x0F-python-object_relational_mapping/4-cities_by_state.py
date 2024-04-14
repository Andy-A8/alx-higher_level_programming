#!/usr/bin/python3
import MySQLdb
import sys
"""
    Lists all cities from the database hbtn_0e_4_usa.
        Takes 3 arguments: mysql username, mysql password database name.
        Stored in ascending order by cities.id
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT 'cities'.'id', 'cities'.'name', 'states'.'name' \
                FROM 'cities' JOIN 'states' ON 'cities'.'state_id' \
                = 'states'.'id' ORDER BY 'cities'.'id' ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
