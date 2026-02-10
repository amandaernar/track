import sqlite3

def start():
    conn = sqlite3.connect('budget.db')
    cur = conn.cursor()

    cur.execute(
        expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            label TEXT,
            amount REAL
            )
        )
    conn.commit()
    conn.close()

def addexpense(date, label, amount):
    conn = sqlite3.connect('budget.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO expenses (date, label, amount) VALUES (?, ?, ?)',
                (date, label, amount))
    conn.commit()
    conn.close()

def getexpense():
    conn = sqlite3.connect('budget.db')
    cur = conn.cursor()
    cur.execute('SELECT date, label, amount FROM expenses')
    rows = cur.fetchall()
    conn.close()
    return rows
