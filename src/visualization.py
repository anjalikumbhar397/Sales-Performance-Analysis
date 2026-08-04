import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("data/cleaned_sales_data.xlsx")
#Monthly sales
monthly_sales =(
    df.groupby("Month")["Total Sales"]
    .sum()
)
month_order =[
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]
Monthly_Sales = monthly_sales.reindex(month_order)

plt.figure(figsize=(12,6))
plt.bar(
    monthly_sales.index, 
    monthly_sales.values
)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_sales.png")
plt.show()

plt.figure(figsize=(12,6))
plt.bar(
    monthly_sales.index,
    monthly_sales.values
)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_sales.png")
plt.show()

#Region-wise sales
regions_sales = (
    df.groupby("Region")["Total Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

plt.bar(
    regions_sales.index,
    regions_sales.values
)
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("charts/regions_sales.png")
plt.show()

#category-wise sales
category_sales =(
    df.groupby("Category")["Total Sales"]
    .sum()
)
plt.figure(figsize=(7,7))

plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Category-wise Sales")
plt.savefig("charts/category_sales.png")
plt.show()

top_products =(
    df.groupby("Product")["Total Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
plt.figure(figsize=(12,6))

plt.bar(
    top_products.index,
    top_products.values
)

plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.show()

salesperson_sales =(
    df.groupby("Salesperson")["Total Sales"]
    .sum()
    .sort_values(ascending=False)
)
plt.figure(figsize=(10,6))
plt.bar(
    salesperson_sales.index,
    salesperson_sales.values
)
plt.title("Salesperson Performance")
plt.xlabel("Salesperson")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/salesperson_performance.png")
plt.show()

monthly_sales =(
    df.groupby("Month")["Total Sales"]
      .sum()
      .reindex(month_order)
)
plt.figure(figsize=(12,6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2
)
plt.title("monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/monthly_sales_trends.png")
plt.show()
print("All charts generated successfully!")
print("Check the 'charts' folder.")