# This program analyzes our sales data
# We'll calculate KPIs and find insights!

import pandas as pd

print("📊 SALES ANALYTICS DASHBOARD")
print("=" * 60)

# STEP 1: Load the Excel file
print("\n🔄 Loading data from sales_data.xlsx...")
df = pd.read_excel('sales_data.xlsx')

print(f"✅ Loaded {len(df)} sales records")

# STEP 2: Calculate KPIs (Key Performance Indicators)
print("\n" + "=" * 60)
print("💰 KEY PERFORMANCE INDICATORS (KPIs)")
print("=" * 60)

total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()
total_orders = len(df)
avg_order_value = df['Revenue'].mean()
profit_margin = (total_profit / total_revenue) * 100

print(f"\n📈 Total Revenue:        ${total_revenue:,.2f}")
print(f"💵 Total Profit:         ${total_profit:,.2f}")
print(f"📦 Total Orders:         {total_orders}")
print(f"🎯 Average Order Value:  ${avg_order_value:.2f}")
print(f"📊 Profit Margin:        {profit_margin:.2f}%")

# STEP 3: Best Performing Region
print("\n" + "=" * 60)
print("🗺️  REGIONAL PERFORMANCE")
print("=" * 60)

# Group by Region and calculate total revenue
region_sales = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)

print("\nRevenue by Region:")
for region, revenue in region_sales.items():
    percentage = (revenue / total_revenue) * 100
    print(f"   {region:10s}  ${revenue:>10,.2f}  ({percentage:>5.1f}%)")

best_region = region_sales.index[0]
print(f"\n🏆 Best Region: {best_region} with ${region_sales[best_region]:,.2f}")

# STEP 4: Top Products
print("\n" + "=" * 60)
print("📦 PRODUCT PERFORMANCE")
print("=" * 60)

# Group by Product and calculate total revenue
product_sales = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

print("\nRevenue by Product:")
for i, (product, revenue) in enumerate(product_sales.items(), 1):
    print(f"   {i}. {product:15s}  ${revenue:>10,.2f}")

best_product = product_sales.index[0]
print(f"\n🏆 Top Product: {best_product} with ${product_sales[best_product]:,.2f}")

# STEP 5: Most Profitable Product
print("\n" + "=" * 60)
print("💎 PROFITABILITY ANALYSIS")
print("=" * 60)

product_profit = df.groupby('Product')['Profit'].sum().sort_values(ascending=False)

print("\nProfit by Product:")
for i, (product, profit) in enumerate(product_profit.items(), 1):
    print(f"   {i}. {product:15s}  ${profit:>10,.2f}")

most_profitable = product_profit.index[0]
print(f"\n💰 Most Profitable: {most_profitable} with ${product_profit[most_profitable]:,.2f} profit")

# STEP 6: Summary Insights
print("\n" + "=" * 60)
print("🔍 KEY INSIGHTS")
print("=" * 60)

print(f"\n1. Our {best_region} region is performing the best!")
print(f"2. {best_product} is our top-selling product")
print(f"3. {most_profitable} generates the most profit")
print(f"4. We're making {profit_margin:.1f}% profit margin overall")

print("\n✅ Analysis Complete!")
print("=" * 60)