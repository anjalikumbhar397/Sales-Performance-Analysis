import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

def load_css():
    css_path = Path(__file__).parent / "styles.css"

    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# ======================================
# LOAD DATA
# ======================================

@st.cache_data
def load_data():
    df = pd.read_excel("data/cleaned_sales_data.xlsx")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# ======================================
# SIDEBAR
# ======================================

st.sidebar.title("🔍 Filters")

region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

salesperson = st.sidebar.selectbox(
    "Salesperson",
    ["All"] + sorted(df["Salesperson"].unique().tolist())
)

customer = st.sidebar.selectbox(
    "Customer Type",
    ["All"] + sorted(df["Customer Type"].unique().tolist())
)

# ======================================
# APPLY FILTERS
# ======================================

filtered_df = df.copy()

if region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region]

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

if salesperson != "All":
    filtered_df = filtered_df[filtered_df["Salesperson"] == salesperson]

if customer != "All":
    filtered_df = filtered_df[filtered_df["Customer Type"] == customer]

# ======================================
# TITLE
# ======================================

st.markdown("""
<div style='background:linear-gradient(90deg,#2563EB,#1D4ED8);
padding:20px;
border-radius:15px;
text-align:center;
color:white;'>

<h1>📊 Sales Performance Dashboard</h1>

<p>Interactive Business Intelligence Dashboard</p>

</div>
""", unsafe_allow_html=True)
st.info(
    "📌 Use the filters in the sidebar to explore sales performance by region, category, salesperson, and customer type."
)
st.divider()
st.subheader("📈 Key Performance Indicators")
# ======================================
# KPI CARDS
# ======================================

total_sales = filtered_df["Total Sales"].sum()
total_orders = len(filtered_df)
average_order = filtered_df["Total Sales"].mean()
highest_sale = filtered_df["Total Sales"].max()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Sales",
    f"₹{total_sales:,.2f}"
)

col2.metric(
    "📦 Orders",
    f"{total_orders:,}"
)

col3.metric(
    "📈 Average Order",
    f"₹{average_order:,.2f}"
)

col4.metric(
    "🏆 Highest Sale",
    f"₹{highest_sale:,.2f}"
)

st.divider()
st.subheader("📅 Monthly Sales Trend")
# ======================================
# MONTHLY SALES TREND
# ======================================

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

monthly_sales = (
    filtered_df.groupby("Month")["Total Sales"]
    .sum()
    .reindex(month_order)
    .reset_index()
)

fig_month = px.line(
    monthly_sales,
    x="Month",
    y="Total Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig_month, use_container_width=True)
st.subheader("🌍 Regional Performance")
# ======================================
# REGION & CATEGORY
# ======================================

col1, col2 = st.columns(2)

with col1:

    region_sales = (
        filtered_df.groupby("Region")["Total Sales"]
        .sum()
        .reset_index()
    )

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="Total Sales",
        color="Region",
        title="Region-wise Sales"
    )

    st.plotly_chart(fig_region, use_container_width=True)

with col2:

    category_sales = (
        filtered_df.groupby("Category")["Total Sales"]
        .sum()
        .reset_index()
    )

    fig_category = px.pie(
        category_sales,
        values="Total Sales",
        names="Category",
        title="Category Distribution"
    )

    st.plotly_chart(fig_category, use_container_width=True)
st.subheader("📦 Product Analysis")
# ======================================
# TOP PRODUCTS
# ======================================

top_products = (
    filtered_df.groupby("Product")["Total Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_products = px.bar(
    top_products,
    x="Product",
    y="Total Sales",
    color="Product",
    title="Top 10 Products"
)

st.plotly_chart(fig_products, use_container_width=True)
st.subheader("👨‍💼 Salesperson Performance")
# ======================================
# SALESPERSON PERFORMANCE
# ======================================

salesperson_sales = (
    filtered_df.groupby("Salesperson")["Total Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_salesperson = px.bar(
    salesperson_sales,
    x="Salesperson",
    y="Total Sales",
    color="Salesperson",
    title="Salesperson Performance"
)

st.plotly_chart(fig_salesperson, use_container_width=True)

# ======================================
# SALES TABLE
# ======================================

st.subheader("📋 Sales Records")

st.write(f"Showing **{len(filtered_df)}** records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# ======================================
# DOWNLOAD BUTTON
# ======================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

# ======================================
# FOOTER
# ======================================

st.divider()

st.caption(
    "Developed using Python • Pandas • Plotly • Streamlit"
)