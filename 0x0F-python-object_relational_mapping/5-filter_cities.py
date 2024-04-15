#!/usr/bin/python3
import MySQLdb
import sys
"""
    Takes in an argument and lists all cities of that state,
        using the database hbtn_0e_4_usa.
    Takes 4 arguments: mysql username, mysql password, database name
        and state name.
    Must be SQL injection free.
    Sorted in ascending order by cities.id
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT 'cities'.'id', 'cities'.'name', \
                FROM 'cities' JOIN 'states' \
                ON 'cities'.'state_id' = 'states'.'id' \
                WHERE 'states'.'name' LIKE BINARY %(state_name)s \
                ORDER BY 'cities'.'id' ASC")
    query_rows = cur.fetchall()

    if query_rows is not None:
        print(", ".join([row[1] for row in query_rows]))

    cur.close()
    db.close()
