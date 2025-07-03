import sqlite3

data = [
    ("Apple",   "2025-07-01", 5,  30.0),
    ("Banana",  "2025-07-01", 8,  12.0),
    ("Orange",  "2025-07-02", 7,  21.0),
    ("Apple",   "2025-07-02", 3,  18.0),
    ("Banana",  "2025-07-03", 2,   3.0),
]

with sqlite3.connect("sales_data.db") as conn:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            product  TEXT,
            sale_dt  TEXT,
            quantity INTEGER,
            price    REAL
        );
    """)
    cur.execute("DELETE FROM sales")
    cur.executemany(
        "INSERT INTO sales(product, sale_dt, quantity, price) VALUES (?,?,?,?)",
        data
    )
    conn.commit()

print("DB initialised with", len(data), "rows.")
