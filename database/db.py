import sqlite3

conn = sqlite3.connect("receipts.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS receipts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    store TEXT,
    date TEXT,
    total REAL
)
""")

conn.commit()


def save_receipt(data):
    cursor.execute("""
    INSERT INTO receipts (store, date, total)
    VALUES (?, ?, ?)
    """, (data["store"], data["date"], data["total"]))

    conn.commit()