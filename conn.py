import psycopg2
#estamos probando git
conn = psycopg2.connect(
    host="ec2-44-198-223-154.compute-1.amazonaws.com",
    database="d6k8pf744iivoh",
    user="glbybbbgetizbw",
    password="4a6d84cd18afa55a53ede162d298b2c6139a0987c0d432558dd91f1d5d5caec6"
)

cur = conn.cursor()

cur.execute('SELECT * FROM rol')

print(cur.fetchall())

cur.close()

