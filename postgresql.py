import psycopg2
conn = psycopg2.connect(database='aa', user='username',
                        password='123456', host='192.168.131.222', port='8888')
cur = conn.cursor()
cur.execute("SELECT * FROM table1 LIMIT 10")
rows = cur.fetchall()
print(rows)
conn.commit()
cur.close()
conn.close()
