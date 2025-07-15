import streamlit as st
from PIL import Image
from datetime import datetime
from modules.sales_manager import SalesManager
import matplotlib.pyplot as plt

# Create an instance of SalesManager connected to the carwash database
manager = SalesManager("C:/learning/sic_pu_june25/Hacker_rank/db/carwash.db")

# Header for the dashboard
st.title("🚗 Car Wash Sales Dashboard")

# --- Monthly Sales Overview ---
st.subheader("Monthly Sales Overview")

# Year picker using unique years in dataset
year = st.selectbox("Select Year", sorted(manager.df['date'].dt.year.unique(), reverse=True))

# Get monthly sales for selected year
monthly_sales = manager.calculate_monthly_sales_year(year)
st.bar_chart(monthly_sales)

# --- Sales by Time Block ---
st.subheader("Sales by Time Block")
time_sales = manager.categorize_time_blocks()
st.write(time_sales)

# Pie chart visualization for sales by time
fig, ax = plt.subplots()
ax.pie(time_sales, labels=time_sales.index, autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution by Time of Day")
st.pyplot(fig)

# --- Inactive Customers ---
st.subheader("Inactive Customers (2+ Months)")
inactive_list = manager.detect_inactive_customers()
st.write(inactive_list)

# --- Valuable Inactive Customers ---
st.subheader("Valuable Inactive Customers")

# Input: minimum total spending to be considered "valuable"
min_amount = st.number_input("Minimum total amount spent", min_value=0, value=100)

# Get valuable inactive customers from manager
valuable_customers = manager.valuable_inactive_customers(days=60, min_total_amount=min_amount)
if not valuable_customers.empty:
    st.dataframe(valuable_customers)
else:
    st.info("No valuable inactive customers found.")

# --- Special Pricing Months ---
st.subheader("Special Pricing Months")

# Identify months for discounts and surcharges
discount_months = manager.months_for_discount()
surcharge_months = manager.months_for_surcharge()
st.markdown(f"**Discount Months:** {discount_months if discount_months else 'None'}")
st.markdown(f"**Surcharge Months:** {surcharge_months if surcharge_months else 'None'}")

# --- Export Pie Chart ---
if st.button("Export Pie Chart Image"):
    try:
        manager.export_pie_chart()
        st.success("Pie chart exported successfully!")
    except Exception as e:
        st.error(f"Export failed: {e}")

# --- Preview Pie Chart ---
st.subheader("Exported Pie Chart Preview")
try:
    image = Image.open("C:/learning/sic_pu_june25/Hacker_rank/charts/sales_pie_chart.png")
    st.image(image, caption="Sales by Time Block", use_column_width=True)
except FileNotFoundError:
    st.warning("Chart not found yet—export it first.")

# --- Monthly Sales by Service ---
st.subheader("Monthly Sales by Service")
sales_by_service = manager.calculate_monthly_sales_by_service(year)
if not sales_by_service.empty:
    st.dataframe(sales_by_service)
    st.line_chart(sales_by_service)
else:
    st.info("No service-wise data available.")