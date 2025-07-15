# ✅ Simple Streamlit dashboard for visualizing car wash sales

# Importing Streamlit for creating web dashboard
import streamlit as st
from modules.sales_manager import SalesManager

# Creating an object to access sales data and functions
manager = SalesManager("C:/learning/sic_pu_june25/Hacker_rank/db/carwash.db")

# Displaying dashboard title
st.title("🧼 Car Wash Sales Dashboard")

# Showing a bar chart of monthly sales totals
st.subheader("📅 Monthly Sales Overview")
monthly = manager.calculate_monthly_sales()
st.bar_chart(monthly)

# Displaying sales amounts by time block (morning, evening, etc.)
st.subheader("🕓 Sales by Time Block")
time_sales = manager.categorize_time_blocks()
st.write(time_sales)

# Listing customers who haven't returned in the last 60 days
st.subheader("🎁 Inactive Customers (2+ Months)")
inactive_list = manager.detect_inactive_customers()
st.write(inactive_list)

# Button that lets user save the pie chart
if st.button("📤 Export Pie Chart"):
    manager.export_pie_chart()
    st.success("✅ Chart exported to charts/sales_pie_chart.png")

# Show the saved pie chart image inside the app
from PIL import Image

st.subheader("🖼 Exported Pie Chart Preview")

try:
    image = Image.open("C:/learning/sic_pu_june25/Hacker_rank/charts/sales_pie_chart.png")
    st.image(image, caption="Sales by Time Block", use_column_width=True)
except FileNotFoundError:
    st.warning("📁 Chart not found yet—export it first using the button above.")