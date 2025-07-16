import pandas as pd
import sqlite3
from datetime import datetime, timedelta

class FoodWastageManager:
    def __init__(self, db_path):
        #  Connect to database and read table into DataFrame
        self.conn = sqlite3.connect(db_path)
        self.df = pd.read_sql_query("SELECT * FROM food_wastage", self.conn)

        #  Normalize column names for consistency
        self.df.columns = [col.strip().lower().replace(" ", "_") for col in self.df.columns]

        #  Ensure 'date' column is in datetime format
        self.df['date'] = pd.to_datetime(self.df['date'])

    def get_daily_wastage(self):
        #  Returns total food wasted per day
        return self.df.groupby('date')['food_wasted'].sum().reset_index()

    def get_wastage_percentage(self):
        # Calculates daily wastage %: wasted / prepared * 100
        self.df['wastage_pct'] = (self.df['food_wasted'] / self.df['food_prepared']) * 100
        return self.df.groupby('date')['wastage_pct'].mean().reset_index()

    def get_avg_wastage_per_student(self):
        #  Average food wasted per student served
        self.df['waste_per_student'] = self.df['food_wasted'] / self.df['students_served']
        return self.df.groupby('date')['waste_per_student'].mean().reset_index()

    def total_food_prepared_consumed_wasted(self):
        # Returns overall totals for food prepared, consumed, and wasted
        return {
            "prepared": self.df['food_prepared'].sum(),
            "consumed": self.df['food_consumed'].sum(),
            "wasted": self.df['food_wasted'].sum()
        }

    def recommend_reduction_tips(self):
        #  Static list of practical tips to reduce wastage
        return [
            "Serve food based on real-time demand to avoid excess preparation.",
            "Encourage students to take only what they can consume.",
            "Reuse leftover edible food safely in other meals or donate.",
            "Educate students on food wastage impact and promote responsible behavior.",
            "Use smaller plates to reduce portion sizes and wastage."
        ]