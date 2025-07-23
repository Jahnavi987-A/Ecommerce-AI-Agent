import pandas as pd
import sqlite3
import os

def load_csv_to_sql():
    os.makedirs("db", exist_ok=True)
    conn = sqlite3.connect('db/ecommerce.db')

    ad_sales = pd.read_csv('Data/ad_sales.csv')
    total_sales = pd.read_csv('Data/total_sales.csv')
    eligibility = pd.read_csv('Data/eligibility.csv')

    ad_sales.to_sql('ad_sales', conn, if_exists='replace', index=False)
    total_sales.to_sql('total_sales', conn, if_exists='replace', index=False)
    eligibility.to_sql('eligibility', conn, if_exists='replace', index=False)

    print("your datasets are loaded into db/ecommerce.db")
    conn.close()

def execute_sql_query(sql: str):
    conn = sqlite3.connect("db/ecommerce.db")
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return [f"SQL Execution Error: {e}"]

if __name__ == "__main__":
    try:
        load_csv_to_sql()
    except Exception as e:
        print("error occurred", e)
