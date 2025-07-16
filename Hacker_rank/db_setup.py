import pandas as pd
import sqlite3

def create_and_populate_db(db_path, csv_path):
    # 📥 Step 1: Read the CSV file
    df = pd.read_csv(csv_path)

    # 🧹 Step 2: Normalize column names (lowercase and underscore)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # 🔌 Step 3: Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 💣 Step 4: Drop existing table (if any) to avoid schema mismatch
    cursor.execute("DROP TABLE IF EXISTS food_wastage")

    # 🏗️ Step 5: Create new table with correct schema
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

    # 📝 Step 6: Insert data into the table using pandas
    df.to_sql("food_wastage", conn, if_exists="append", index=False)

    # ✅ Step 7: Finalize and close
    conn.commit()
    conn.close()
    print(f"✅ Database created and populated successfully at: {db_path}")

# 🚀 Main entry point to execute setup
if __name__ == "__main__":
    create_and_populate_db("food_wastage.db", "food_wastage.csv")