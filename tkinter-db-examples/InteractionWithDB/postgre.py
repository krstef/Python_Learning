import psycopg2 as ps

def create_table():
    conn = ps.connect("dbname='test1' user='user1'  password='123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    return 1

def insert_in_table(item, quantity, price):
    conn = ps.connect("dbname='test1' user='user1'  password='123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = ps.connect("dbname='test1' user='user1'  password='123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = ps.connect("dbname='test1' user='user1'  password='123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = ps.connect("dbname='test1' user='user1'  password='123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

if(create_table()):
    insert_in_table("Orange", 50, 7)
    #delete("Orange")
    update(15, 10.5, "Water glass")
    update(70, 6, "Orange")
print(view())
