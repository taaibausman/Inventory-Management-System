import sqlite3 as sq

def create_db():
    con = sq.connect(database=r'ims.db')
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS category (
            Category_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            dob TEXT,
            doj TEXT,
            pass TEXT,
            utype TEXT,
            address TEXT,
            salary TEXT
        )
    """)
    cur.execute('''
            CREATE TABLE IF NOT EXISTS supplier (
                invoice TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                contact TEXT,
                email TEXT,
                desc TEXT
            )
        ''')
    
    cur.execute('''
    CREATE TABLE IF NOT EXISTS product (
        pid INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        supplier TEXT NOT NULL,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        qty INTEGER NOT NULL,
        status TEXT NOT NULL
    )
    ''')
    cur.execute("""
    CREATE TABLE IF NOT EXISTS register(
        f_name TEXT,
        username TEXT,
        contact TEXT,
        email TEXT,
        sec_ques TEXT,
        sec_ans TEXT,
        password TEXT
    )
""")
    con.commit()
    con.close()
create_db()