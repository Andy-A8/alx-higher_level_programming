#!/usr/bin/python3
import MySQLdb
import sys
"""
    Lists all states with a name starting with n (UPPER N)
    from the database hbtn_0e_0_usa.
        Takes 3 arguments: mysql username, mysql password database name.
        Stored in ascending order by states.id
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT 'id', 'name' FROM 'states' ORDER BY 'states.id' ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()
