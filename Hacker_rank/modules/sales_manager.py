import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Class to manage sales-related queries and visualizations
class SalesManager:
    def __init__(self, db_path):
        # Load the sales data from the database on initialization
        self.conn = sqlite3.connect(db_path)
        self.df = pd.read_sql_query("SELECT * FROM sales", self.conn)
        
        # Convert date column to proper datetime format
        self.df['date'] = pd.to_datetime(self.df['date'])

    def calculate_monthly_sales(self, year=None):
        # Calculates total sales per month, optionally filtered by year
        df = self.df
        if year is not None:
            df = df[df['date'].dt.year == year]
        return df.groupby(df['date'].dt.month)['amount'].sum()

    def calculate_monthly_sales_year(self, year):
        # Alias for calculate_monthly_sales with mandatory year input
        return self.calculate_monthly_sales(year)

    def calculate_monthly_sales_by_service(self, year=None):
        # Calculates monthly sales totals broken down by service ID
        if self.df.empty:
            return pd.DataFrame()
        df = self.df.copy()
        if year is not None:
            df = df[df['date'].dt.year == year]
        df['month'] = df['date'].dt.month
        grouped = df.groupby(['month', 'service_id'])['amount'].sum().reset_index()
        return grouped.pivot(index='month', columns='service_id', values='amount').fillna(0)

    def categorize_time_blocks(self):
        # Groups sales into 4 time blocks: Night, Morning, Afternoon, Evening
        df = self.df.copy()
        df['hour'] = df['date'].dt.hour
        df['time_block'] = pd.cut(
            df['hour'],
            bins=[0, 6, 12, 18, 24],
            labels=['Night', 'Morning', 'Afternoon', 'Evening'],
            include_lowest=True,
            right=False
        )
        return df.groupby('time_block')['amount'].sum()

    def detect_inactive_customers(self, days=60):
        # Finds customers who haven't returned in the last `days` days
        last_seen = self.df.groupby('cust_id')['date'].max()
        cutoff = datetime.now() - timedelta(days=days)
        return last_seen[last_seen < cutoff].index.tolist()

    def valuable_inactive_customers(self, days=60, min_total_amount=100):
        # Identifies inactive customers who spent more than the minimum amount
        last_seen = self.df.groupby('cust_id')['date'].max()
        cutoff = datetime.now() - timedelta(days=days)
        inactive_ids = last_seen[last_seen < cutoff].index
        total_spent = self.df[self.df['cust_id'].isin(inactive_ids)].groupby('cust_id')['amount'].sum()
        valuable = total_spent[total_spent >= min_total_amount]
        return valuable.reset_index().rename(columns={'amount': 'total_spent'})

    def months_for_discount(self, threshold=0.85):
        # Returns months with low sales (under 85% of average) for potential discounts
        monthly = self.df.groupby(self.df['date'].dt.month)['amount'].sum()
        avg = monthly.mean()
        return monthly[monthly < avg * threshold].index.tolist()

    def months_for_surcharge(self, threshold=1.15):
        # Returns months with high sales (above 115% of average) for surcharges
        monthly = self.df.groupby(self.df['date'].dt.month)['amount'].sum()
        avg = monthly.mean()
        return monthly[monthly > avg * threshold].index.tolist()

    def export_pie_chart(self, output_path='C:/learning/sic_pu_june25/Hacker_rank/charts/sales_pie_chart.png'):
        # Saves a pie chart of sales by time block to the specified path
        sales_by_time = self.categorize_time_blocks()
        fig, ax = plt.subplots()
        ax.pie(sales_by_time, labels=sales_by_time.index, autopct='%1.1f%%', startangle=90)
        plt.title("Sales Distribution by Time of Day")
        fig.savefig(output_path)
        plt.close(fig)