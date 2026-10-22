import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("Lab 7: Interactive Sales Dashboard")
st.write("Analyze sales using interactive filters and charts.")

# Sample sales data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet"],
    "Region": ["South", "North", "East", "West", "South", "North"],
    "Sales": [50000, 30000, 20000, 45000, 35000, 25000],
    "Quantity": [5, 10, 4, 4, 12, 5]
}

df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=list(df["Region"].unique())
)

products = st.sidebar.multiselect(
    "Select Product",
    options=df["Product"].unique(),
    default=list(df["Product"].unique())
)

filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Product"].isin(products))
]

# Summary metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"₹{filtered_df['Sales'].sum():,}")

with col2:
    st.metric("Total Quantity", int(filtered_df["Quantity"].sum()))

with col3:
    st.metric("Number of Records", len(filtered_df))

# Data table
st.subheader("Sales Data")
st.dataframe(filtered_df, use_container_width=True)

# Charts
if not filtered_df.empty:
    st.subheader("Sales by Product")
    product_sales = filtered_df.groupby("Product")["Sales"].sum()
    st.bar_chart(product_sales)

    st.subheader("Sales by Region")
    region_sales = filtered_df.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)
else:
    st.warning("No sales records match your selected filters.")