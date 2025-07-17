import pandas as pd
import sqlite3
import os

def create_and_populate_db(db_path, csv_path):
    # Step 1: Check if CSV exists before reading
    if not os.path.exists(csv_path):
        print(f"❌ File not found: {csv_path}")
        return

    # Step 2: Read the CSV file
    df = pd.read_csv(csv_path)

    # Step 3: Normalize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Step 4: Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Step 5: Drop existing table to avoid schema mismatch
    cursor.execute("DROP TABLE IF EXISTS food_wastage")

    # Step 6: Create table
    cursor.execute("""
        CREATE TABLE food_wastage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            food_prepared INTEGER,
            food_consumed INTEGER,
            food_wasted INTEGER,
            students_served INTEGER
        )
    """)

    # Step 7: Insert data
    df.to_sql("food_wastage", conn, if_exists="append", index=False)

    # Step 8: Finalize
    conn.commit()
    conn.close()
    print(f"✅ Database created and populated successfully at: {db_path}")

# Main entry point
if __name__ == "__main__":
    create_and_populate_db(
        "food_wastage.db",
        r"C:\learning\sic_pu_june25\hackathon_food\codes\food_wastage.csv"
    )