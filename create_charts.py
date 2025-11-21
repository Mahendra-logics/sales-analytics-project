# This program creates visual charts from our sales data
# Visualization = Turning numbers into pictures!

import pandas as pd
import matplotlib.pyplot as plt

print("📊 Creating visualizations...")

# Load data
df = pd.read_excel('sales_data.xlsx')

# Create folder for charts
import os
os.makedirs('charts', exist_ok=True)

# CHART 1: Revenue by Region
print("\n📊 Creating Chart 1: Revenue by Region...")

region_sales = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))  # Size of chart
plt.bar(region_sales.index, region_sales.values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
plt.title('Revenue by Region', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(region_sales.values):
    plt.text(i, v, f'${v:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('charts/revenue_by_region.png', dpi=300, bbox_inches='tight')
print("   ✅ Saved: charts/revenue_by_region.png")
plt.close()

# CHART 2: Revenue by Product
print("\n📊 Creating Chart 2: Revenue by Product...")

product_sales = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(14, 7))  # Bigger size
plt.barh(product_sales.index, product_sales.values, color='#4ECDC4')
plt.title('Revenue by Product', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Revenue ($)', fontsize=12)
plt.ylabel('Product', fontsize=12)
plt.grid(axis='x', alpha=0.3)

# Add value labels INSIDE the bars (on the right)
for i, v in enumerate(product_sales.values):
    plt.text(v - 8000, i, f'${v:,.0f}', va='center', ha='right', fontweight='bold', color='white', fontsize=11)

# Add more space on the right
plt.xlim(0, product_sales.max() * 1.1)  # 10% extra space

plt.tight_layout()
plt.savefig('charts/revenue_by_product.png', dpi=300, bbox_inches='tight')
print("   ✅ Saved: charts/revenue_by_product.png")
plt.close() 

# CHART 3: Region Distribution (Pie Chart)
print("\n📊 Creating Chart 3: Regional Distribution...")

plt.figure(figsize=(10, 8))
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
plt.pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%', 
        colors=colors, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
plt.title('Sales Distribution by Region', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/region_distribution.png', dpi=300, bbox_inches='tight')
print("   ✅ Saved: charts/region_distribution.png")
plt.close()

print("\n✅ All charts created successfully!")
print("📁 Check the 'charts' folder to see your visualizations!")