#!/usr/bin/python3

"""
    task 1
"""

if __name__ == '__main__':

    import sys
    import MySQLdb as mysqldb

    host = 'localhost'
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    port = 3306

    config = {
        'host': 'localhost',
        'user': username,
        'passwd': password,
        'db': dbname,
        'port': port
    }

    db = mysqldb.connect(**config)

    cur = db.cursor()

    query = 'SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id ASC'
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
