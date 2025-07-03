"""
Pull basic sales summaries from a SQLite DB and plot revenue per product.
Run:  python sales_summary.py
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "sales_data.db"

# 1️⃣  Connect
conn = sqlite3.connect(DB_PATH)

# 2️⃣  Query 1: per‑product summary
summary_q = """
SELECT
    product,
    SUM(quantity)                 AS total_qty,
    ROUND(SUM(quantity * price),1) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
"""
summary_df = pd.read_sql_query(summary_q, conn)

# 3️⃣  Query 2: overall totals (nice but optional)
totals_q = """
SELECT
    SUM(quantity)                 AS grand_qty,
    ROUND(SUM(quantity * price),1) AS grand_revenue
FROM sales;
"""
totals = pd.read_sql_query(totals_q, conn).iloc[0]

conn.close()

# 4️⃣  Print to console
print("\n=== Per‑product summary ===")
print(summary_df.to_string(index=False))
print("\n=== Grand totals ===")
print(f"Total units sold : {totals.grand_qty}")
print(f"Total revenue    : ₹{totals.grand_revenue:,.2f}")

# 5️⃣  Bar chart (revenue per product)
ax = summary_df.plot(kind="bar", x="product", y="revenue", legend=False)
ax.set_ylabel("Revenue (₹)")
ax.set_title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart.png")   # autosave for GitHub
plt.show()
