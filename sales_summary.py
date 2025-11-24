# ------------------ Step 1: Import Libraries ------------------
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ------------------ Step 2: Connect to SQLite Database ------------------
conn = sqlite3.connect("sales_data.db")  # Creates file if not exists
cursor = conn.cursor()

# ------------------ Step 3: Create Table & Insert Sample Data ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Clear old data (optional)
cursor.execute("DELETE FROM sales")

# Sample data
sample_data = [
    ('Pen', 10, 5),
    ('Pencil', 15, 2),
    ('Notebook', 5, 20)
]

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?)", sample_data)
conn.commit()

# ------------------ Step 4: SQL Query ------------------
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# ------------------ Step 5: Load into Pandas & Print ------------------
df = pd.read_sql_query(query, conn)
print(df)

# ------------------ Step 6: Plot Bar Chart ------------------
df.plot(kind='bar', x='product', y='revenue', title='Revenue per Product')
plt.ylabel("Revenue")
plt.show()

# ------------------ Step 7: Close Connection ------------------
conn.close()
