import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df = pd.read_excel("data/cleaned_sales_data.xlsx")

monthly_sales = (
    df.groupby("Month")["Total Sales"]
    .sum()
    .reset_index()
)
print(df.columns)
month_map = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

monthly_sales["Month Number"] = monthly_sales["Month"].map(month_map)

monthly_sales = monthly_sales.sort_values("Month Number")
X = monthly_sales[["Month Number"]]
y = monthly_sales["Total Sales"]
model = LinearRegression()
model.fit(X,y)
monthly_sales["Predicted Sales"] = model.predict(X)

future_months = pd.DataFrame({
    "Month Number":[13,14,15]
})
future_predictions =model.predict(future_months)
future_df = pd.DataFrame({
    "Month  Number": [13,14,15],
    "Predicted Sales": future_predictions
})
print(future_df)
future_df.to_excel(
    "output/sales_forecast.xlsx",
    index=False
)
plt.figure(figsize=(10,6))

plt.plot(
    monthly_sales["Month Number"],
    monthly_sales["Total Sales"],
    marker="o",
    label="Actual Sales"
)

plt.plot(
    monthly_sales["Month Number"],
    monthly_sales["Predicted Sales"],
    marker="s",
    linestyle="--",
    label="Predicted Sales"
)

plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.title("Sales Forecast")

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig("charts/sales_forecast.png")

plt.show()
print("Sales forecasting completed successfully!")
print("Forecast saved in output/sales_forecast.xlsx")