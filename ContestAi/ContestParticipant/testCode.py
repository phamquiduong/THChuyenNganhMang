import sqlite3

try:
    conn = sqlite3.connect('./db.sqlite3')
    cmd = 'SELECT * FROM ContestAdmin_account'
    data = conn.execute(cmd)
    for row in data:
        print(row)
except EOFError as e:
    print (e)