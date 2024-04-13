#!/usr/bin/python3
import MySQLdb
import sys
"""
    Takes in an argument and displays all values in the states table of
        hbtn_0e_0_usa where name matches the argument.
    Must be safe from MySQL injections!
    Takes 4 arguments: mysql username, mysql password database name
        and state name searched.
    Stored in ascending order by states.id
"""

if __name__ == "__main__":
    for c in sys.argv[4]:
        if c == ',':
            exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT 'id', 'name' FROM 'states' WHERE BINARY 'name' = '{}' \
                ORDER BY 'states.id' ASC".format(sys.argv[4]))
    query_row = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
