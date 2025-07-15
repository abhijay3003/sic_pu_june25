import pandas as pd
import sqlite3

def import_csv_to_db(csv_path, db_path, table_name="sales"):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    import_csv_to_db(
        csv_path='C:/learning/sic_pu_june25/Hacker_rank/data/car_wash_sales.csv',
        db_path='C:/learning/sic_pu_june25/Hacker_rank/db/carwash.db'
    )
    print("✅ Database setup complete.")