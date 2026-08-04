import pandas as pd
import random
from datetime import datetime, timedelta
products =[
    "Laptop",
    "Smartphone",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Printer",
    "Headphones",
    "Camera",
    "Smartwatch"
]

categories =["Electronics",
             "Accessories",
             "Office Equipment"
             ]
regions = ["North",
           "South",
           "East",
           "West"]
salespersons = ["Rahul",
                "Priya",
                "Amit",
                "Neha",
                "Arjun",
                "Sneha",
                "Vikram",
                "Pooja"
]

payment_methods = ["Credit Card",
                   "Debit Card",
                   "Cash",
                   "UPI",
                   "Net banking"
]

customer_types =["New",
                 "Returning"]
product_categories = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Monitor": "Electronics",
    "Keyboard": "Accessories",
    "Mouse": "Accessories",
    "Printer": "Office Equipment",
    "Headphones": "Accessories",
    "Camera": "Electronics",
    "Smartwatch": "Electronics"
}
number_of_records = 5000
sales_data = []
start_date = datetime(2025, 1, 1)

for i in range(number_of_records):

    order_id = f"ORD{1000 + i}"

    date = start_date + timedelta(days=random.randint(0, 364))

    product = random.choice(products)

    category = product_categories[product]

    region = random.choice(regions)

    salesperson = random.choice(salespersons)

    units_sold = random.randint(1, 10)

    unit_price = random.randint(100, 2000)

    discount = random.choice([0, 5, 10, 15, 20])

    payment_method = random.choice(payment_methods)

    customer_type = random.choice(customer_types)

    total_sales = units_sold * unit_price * (1 - discount / 100)

    sales_data.append({
        "Order ID": order_id,
        "Date": date.strftime("%Y-%m-%d"),
        "Product": product,
        "Category": category,
        "Region": region,
        "Salesperson": salesperson,
        "Units Sold": units_sold,
        "Unit Price": unit_price,
        "Discount (%)": discount,
        "Total Sales": round(total_sales, 2),
        "Payment Method": payment_method,
        "Customer Type": customer_type
    })

    df = pd.DataFrame(sales_data)
    print(df.head())
    df.to_excel("data/sales_data.xlsx", index=False)
    print("\nDataset Generated Successfully!")
    print("Location : data/sales_data.xlsx")
    print(f"Total Records : {len(df)}")
