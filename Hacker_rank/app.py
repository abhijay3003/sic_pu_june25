import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from food_wastage_manager import FoodWastageManager  # Custom module for managing food data

# 🎛️ Initialize manager to access food wastage data from SQLite database
manager = FoodWastageManager("food_wastage.db")

# 🚀 Set page layout and title
st.set_page_config(page_title="Hostel Food Wastage Dashboard", layout="wide")
st.title("🍽️ College Hostel Food Wastage Dashboard")

# 🔢 SECTION 1 — Summary of Totals
st.subheader("Total Food Prepared, Consumed, and Wasted")
food_totals = manager.total_food_prepared_consumed_wasted()
st.metric("🍳 Food Prepared", f"{food_totals['prepared']} units")
st.metric("🥣 Food Consumed", f"{food_totals['consumed']} units")
st.metric("🗑️ Food Wasted", f"{food_totals['wasted']} units")

st.divider()

# Utility function to show compact line chart
def compact_line_chart(data, title, ylabel):
    fig, ax = plt.subplots(figsize=(4.5, 2.5))  # width x height in inches
    ax.plot(data.index, data.iloc[:, 0], marker='o', linewidth=1)
    ax.set_title(title, fontsize=5)
    ax.set_ylabel(ylabel, fontsize=4)
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)
    st.pyplot(fig)

# 📅 Daily Food Prepared
st.subheader("📅 Daily Food Prepared")
prepared_daily = manager.df[['date', 'food_prepared']].set_index('date')
compact_line_chart(prepared_daily, "Daily Food Prepared", "Units")

# 🥣 Daily Food Consumed
st.subheader("📅 Daily Food Consumed")
consumed_daily = manager.df[['date', 'food_consumed']].set_index('date')
compact_line_chart(consumed_daily, "Daily Food Consumed", "Units")

# 🗑️ Daily Food Wasted
st.subheader("📅 Daily Food Wasted")
wasted_daily = manager.get_daily_wastage().set_index('date')
compact_line_chart(wasted_daily, "Daily Food Wasted", "Units")

# 👥 Students Served Per Day
st.subheader("👥 Daily Students Served")
students_served_daily = manager.df[['date', 'students_served']].set_index('date')
compact_line_chart(students_served_daily, "Students Served", "Count")

# 🍽️ Average Waste Per Student
st.subheader("📊 Average Food Wasted per Student")
avg_waste_daily = manager.get_avg_wastage_per_student().set_index('date')
compact_line_chart(avg_waste_daily, "Waste per Student", "Units")

# 🚨 High Wastage Threshold Detection
st.subheader("🚨 High Wastage Alert")
threshold_limit = st.slider("Set Wastage Threshold (units)", min_value=10, max_value=120, value=30)
days_exceeding_threshold = wasted_daily[wasted_daily['food_wasted'] > threshold_limit]

if days_exceeding_threshold.empty:
    st.success("✅ No days exceeded the selected wastage threshold.")
else:
    st.warning("⚠️ Days with High Wastage:")
    st.dataframe(days_exceeding_threshold)

# 🏆 Top 5 Days of Highest Food Wastage
st.subheader("🏆 Top 5 Days of Highest Food Wastage")
top_5_days = wasted_daily.sort_values(by='food_wasted', ascending=False).head(5)
st.table(top_5_days)

# 💡 Tips to Reduce Wastage
st.subheader("💡 Tips for Reducing Food Wastage")
for tip in manager.recommend_reduction_tips():
    st.write(f"• {tip}")

# 📌 Summary Status
st.subheader("📌 Summary Indicator")
if food_totals['wasted'] > food_totals['prepared'] * 0.10:
    st.warning("⚠️ Over 10% of prepared food is being wasted. Consider adjusting preparation or serving strategy.")
else:
    st.success("✅ Food wastage is well within control. Keep monitoring and improving!")