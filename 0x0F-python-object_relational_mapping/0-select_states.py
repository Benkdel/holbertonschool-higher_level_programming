#!/usr/bin/python3

"""
    task 0
"""

if __name__ == '__main__':

    import sys
    import MySQLdb as mysqldb

    host = 'localhost'
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    port = 3306

    db = mysqldb.connect(host=host, user=username, passwd=password, db=dbname, port=port)

    cur = db.cursor()

    cur.execute("SELECT * FROm states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)


    cur.close()
    db.close()





