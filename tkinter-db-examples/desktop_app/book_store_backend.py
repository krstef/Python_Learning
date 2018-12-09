import sqlite3

# Model part
def connect_to_db():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, \
     title text, author text, year integer, isbn integer)")
    con.commit()
    con.close()

def insert(title, author, year, isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    #NULL means that python will auto increment id
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year,\
     isbn))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    # here we don't have commit method because are not doing any changes to db,\
    #just fetching the data
    con.close()
    return rows

"""
user can request search only by one param, not by all
in that case this function can break out if we don't pass any arguments to it
so, the default values are empty characters:
    this means that if we call this func with title argument, it will search
    db with title argument and with all other arguments which are equal to ""
    in other words - we will search db only by passed argument
"""
def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR \
     isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    #NULL means that python will auto increment id
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()

def update(id,title, author, year, isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    #NULL means that python will auto increment id
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",\
    (title, author, year, isbn, id))
    con.commit()
    con.close()


connect_to_db()
#insert("I like you", "John Terry", 2015, 99)
#delete(2)
#update(3,"Take a look at your team mate wife", "John Terry", 2018, 101)
#print(view(), "\n")
#print(search(year="2015"))
