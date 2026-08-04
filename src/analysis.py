import pandas as pd
df = pd.read_excel("data/cleaned_sales_data.xlsx")
print("=" * 60)
print("SALES PERFORMANCE ANALYSIS")
print("=" * 60)
total_sales = df["Total Sales"].sum()
print(f"\nTotal Sales: ₹{total_sales:,.2f}")
total_orders = len(df)
print(f"\nTotal Orders: {total_orders}")
average_order = df["Total Sales"].mean()
print(f"Average Order Value: ₹{average_order:,.2f}")
highest_sale = df["Total Sales"].max()
print(f"Highest Sale: ₹{highest_sale:,.2f}")
lowest_sale = df["Total Sales"].min()
print(f"Lowest Sale: ₹{lowest_sale:,.2f}")
monthly_sales = (
    df.groupby("Month")["Total Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nMonthly Sales")
print(monthly_sales)

region_sales = (
    df.groupby("Region")["Total Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nRegion-wise Sales")
print(region_sales)
category_sales = (
    df.groupby("Category")["Total Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nCategory-wise Sales")
print(category_sales)
top_products = (
    df.groupby("Product")["Total Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop Products")
print(top_products)
salesperson_sales = (
    df.groupby("Salesperson")["Total Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nSalesperson Performance")
print(salesperson_sales)
monthly_sales.to_excel("output/monthly_sales.xlsx")
region_sales.to_excel("output/region_sales.xlsx")
category_sales.to_excel("output/category_sales.xlsx")
top_products.to_excel("output/top_products.xlsx")
salesperson_sales.to_excel("output/salesperson_sales.xlsx")
print("\nAnalysis Completed Successfully!")
print("Reports saved in the output folder.")

