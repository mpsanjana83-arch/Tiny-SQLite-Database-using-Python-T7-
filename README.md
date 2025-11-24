# Tiny-SQLite-Database-using-Python-T7-
 Get Basic Sales Summary from a Tiny SQLite Database using Python

## **Objective**

The goal of this task is to **use SQL inside Python** to pull basic sales information (like total quantity sold and total revenue) from a small SQLite database and display it using both a **table** and a **bar chart**.

---

## **Tools Used**

* **Python** (with `sqlite3`, `pandas`, `matplotlib`)
* **SQLite** (built into Python)
* **VS Code** or any Python IDE

---

## **Dataset**

A small SQLite database `sales_data.db` was created with a single table `sales`.

**Table Structure:**

| Column   | Type    | Description         |
| -------- | ------- | ------------------- |
| product  | TEXT    | Name of the product |
| quantity | INTEGER | Quantity sold       |
| price    | REAL    | Price per unit      |

**Sample Data:**

| product  | quantity | price |
| -------- | -------- | ----- |
| Pen      | 10       | 5     |
| Pencil   | 15       | 2     |
| Notebook | 5        | 20    |

---

## **Implementation Steps**

1. **Import Libraries**

   ```python
   import sqlite3
   import pandas as pd
   import matplotlib.pyplot as plt
   ```

2. **Connect to SQLite Database**

   ```python
   conn = sqlite3.connect("sales_data.db")
   ```

3. **Create Table & Insert Sample Data**

   * Create table `sales` if it doesn’t exist.
   * Insert sample sales data.

4. **Run SQL Query**

   ```sql
   SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
   FROM sales
   GROUP BY product
   ```

5. **Load Data into Pandas & Print**

   ```python
   df = pd.read_sql_query(query, conn)
   print(df)
   ```

6. **Plot Revenue Bar Chart**

   ```python
   df.plot(kind='bar', x='product', y='revenue', title='Revenue per Product')
   plt.show()
   ```

7. **Close Database Connection**

   ```python
   conn.close()
   ```

---

## **Output**

* **Table:** Shows total quantity and total revenue per product.
* **Bar Chart:** Displays revenue for each product visually.

**Example Revenue Values:**

| product  | total_qty | revenue |
| -------- | --------- | ------- |
| Notebook | 5         | 100     |
| Pen      | 10        | 50      |
| Pencil   | 15        | 30      |

The chart correctly represents the revenue values.

---

## **Learning Outcomes**

By completing this task, I learned:

* How to **write basic SQL queries**.
* How to **connect SQLite database with Python**.
* How to **summarize data using SQL and Pandas**.
* How to **create a simple bar chart** with Matplotlib.

---

## **Files in this Project**

* `sales_summary.py` – Python script performing all operations.
* `sales_data.db` – SQLite database with sales data.
* `sales_chart.png` – Saved bar chart of revenue (optional).


