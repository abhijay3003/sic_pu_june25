#  Loads CSV and stores data in SQLite database

# Importing necessary libraries for loading and storing data
import pandas as pd
import sqlite3

# File path to CSV input and SQLite output
csv_path = 'C:/learning/sic_pu_june25/Hacker_rank/data/car_wash_sales.csv'
db_path = 'C:/learning/sic_pu_june25/Hacker_rank/db/carwash.db'

# Read CSV file into pandas DataFrame
df = pd.read_csv(csv_path)

# Connect to SQLite database and write data as 'sales' table
conn = sqlite3.connect(db_path)
df.to_sql('sales', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

# Print message when setup is complete
print(" Database setup complete.")