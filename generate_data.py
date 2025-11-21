# This program generates fake sales data for practice
# It's like creating a practice dataset to learn with!

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

print("🚀 Starting to create sales data...")
print("=" * 50)

# STEP 1: Define what we sell
# These are our product categories
products = {
    'Laptop': 899.99,      # Product name: Price
    'Smartphone': 699.99,
    'Tablet': 499.99,
    'Headphones': 149.99,
    'Yoga Mat': 39.99,
    'Dumbbells': 79.99,
    'Blender': 89.99,
    'Coffee Maker': 129.99
}

# STEP 2: Define our sales regions
regions = ['North', 'South', 'East', 'West']

# STEP 3: Generate 500 sales records
# We'll create 500 fake customer orders
print("\n📊 Generating 500 sales records...")

all_sales = []  # Empty list to store all our sales

for i in range(500):  # Loop 500 times
    # Pick random product
    product_name = random.choice(list(products.keys()))
    base_price = products[product_name]
    
    # Create one sale record
    sale = {
        'Order_ID': f'ORD-{10000 + i}',  # ORD-10000, ORD-10001, etc.
        'Date': datetime(2024, 1, 1) + timedelta(days=random.randint(0, 300)),  # Random date in 2024
        'Product': product_name,
        'Region': random.choice(regions),
        'Quantity': random.randint(1, 5),  # Buy 1-5 items
        'Unit_Price': base_price,
    }
    
    # Calculate revenue and profit
    sale['Revenue'] = sale['Unit_Price'] * sale['Quantity']
    sale['Profit'] = sale['Revenue'] * random.uniform(0.2, 0.4)  # 20-40% profit margin
    
    all_sales.append(sale)  # Add this sale to our list

# STEP 4: Convert list to DataFrame (Excel-like table)
df = pd.DataFrame(all_sales)

# STEP 5: Sort by date (oldest to newest)
df = df.sort_values('Date').reset_index(drop=True)

# STEP 6: Save to Excel file
filename = 'sales_data.xlsx'
df.to_excel(filename, index=False)

# STEP 7: Show summary
print("=" * 50)
print("✅ SUCCESS! Data generated successfully!")
print("=" * 50)
print(f"\n📈 SUMMARY:")
print(f"   • Total Orders: {len(df)}")
print(f"   • Total Revenue: ${df['Revenue'].sum():,.2f}")
print(f"   • Total Profit: ${df['Profit'].sum():,.2f}")
print(f"   • Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"\n💾 Saved to: {filename}")
print("\n🎉 First 5 records:")
print(df.head())