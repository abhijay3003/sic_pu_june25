# Importing necessary Python libraries
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Creating a class to manage car wash sales data
class SalesManager:
    # When an object is created, connect to the database and load the sales data
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.df = pd.read_sql_query("SELECT * FROM sales", self.conn)
        self.df['date'] = pd.to_datetime(self.df['date'])  # Convert string dates to datetime format

    # Calculate total sales amount for each month
    def calculate_monthly_sales(self):
        return self.df.groupby(self.df['date'].dt.month)['amount'].sum()

    # Group sales into time blocks based on hour of the day
    def categorize_time_blocks(self):
        self.df['hour'] = self.df['date'].dt.hour
        self.df['time_block'] = pd.cut(
            self.df['hour'],
            bins=[0, 6, 12, 18, 24],
            labels=['Night', 'Morning', 'Afternoon', 'Evening'],
            include_lowest=True
        )
        return self.df.groupby('time_block')['amount'].sum()

    # Find customers who haven't visited recently
    def detect_inactive_customers(self, days=60):
        last_seen = self.df.groupby('cust_id')['date'].max()
        cutoff_date = datetime.now() - timedelta(days=days)
        return last_seen[last_seen < cutoff_date].index.tolist()

    # Save a pie chart image showing sales by time block
    def export_pie_chart(self, output_path='C:/learning/sic_pu_june25/Hacker_rank/charts/sales_pie_chart.png'):
        sales_by_time = self.categorize_time_blocks()
        fig, ax = plt.subplots()
        ax.pie(sales_by_time, labels=sales_by_time.index, autopct='%1.1f%%')
        plt.title("Sales Distribution by Time of Day")
        fig.savefig(output_path)
        plt.close(fig)