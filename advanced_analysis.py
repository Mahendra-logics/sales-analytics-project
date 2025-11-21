# Advanced Sales Analysis - Deep dive into patterns!

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("🔍 ADVANCED SALES ANALYSIS")
print("=" * 60)

# Load data
df = pd.read_excel('sales_data.xlsx')
df['Date'] = pd.to_datetime(df['Date'])

# Add time-based columns
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.month_name()
df['Quarter'] = df['Date'].dt.quarter
df['Day_of_Week'] = df['Date'].dt.day_name()

# ANALYSIS 1: Monthly Performance
print("\n📅 MONTHLY PERFORMANCE")
print("=" * 60)

monthly_perf = df.groupby('Month_Name')['Revenue'].agg(['sum', 'mean', 'count'])
monthly_perf = monthly_perf.reindex(['January', 'February', 'March', 'April', 
                                      'May', 'June', 'July', 'August', 
                                      'September', 'October', 'November', 'December'])
monthly_perf = monthly_perf.dropna()

print("\nRevenue by Month:")
for month, row in monthly_perf.iterrows():
    print(f"{month:12s} → Revenue: ${row['sum']:>10,.2f}  |  Orders: {int(row['count']):>3}  |  Avg: ${row['mean']:>8,.2f}")

best_month = monthly_perf['sum'].idxmax()
worst_month = monthly_perf['sum'].idxmin()
print(f"\n🏆 Best Month: {best_month} (${monthly_perf.loc[best_month, 'sum']:,.2f})")
print(f"📉 Worst Month: {worst_month} (${monthly_perf.loc[worst_month, 'sum']:,.2f})")

# ANALYSIS 2: Quarterly Performance
print("\n" + "=" * 60)
print("📊 QUARTERLY BREAKDOWN")
print("=" * 60)

quarterly = df.groupby('Quarter').agg({
    'Revenue': 'sum',
    'Profit': 'sum',
    'Order_ID': 'count'
}).rename(columns={'Order_ID': 'Orders'})

quarterly['Profit_Margin'] = (quarterly['Profit'] / quarterly['Revenue']) * 100

print("\nQuarterly Performance:")
for quarter, row in quarterly.iterrows():
    print(f"Q{quarter}: Revenue ${row['Revenue']:>10,.2f}  |  Profit ${row['Profit']:>10,.2f}  |  Margin {row['Profit_Margin']:.2f}%  |  Orders {int(row['Orders'])}")

# ANALYSIS 3: Product Category Analysis
print("\n" + "=" * 60)
print("💎 PRODUCT PROFITABILITY RANKING")
print("=" * 60)

product_profit = df.groupby('Product').agg({
    'Revenue': 'sum',
    'Profit': 'sum',
    'Order_ID': 'count'
}).rename(columns={'Order_ID': 'Orders'})

product_profit['Profit_Margin'] = (product_profit['Profit'] / product_profit['Revenue']) * 100
product_profit['Avg_Order_Value'] = product_profit['Revenue'] / product_profit['Orders']

product_profit = product_profit.sort_values('Profit', ascending=False)

print("\nProduct Profitability:")
print(f"{'Product':<15} {'Revenue':>12} {'Profit':>12} {'Margin':>8} {'Orders':>7} {'Avg Order':>12}")
print("-" * 75)

for product, row in product_profit.iterrows():
    print(f"{product:<15} ${row['Revenue']:>10,.2f} ${row['Profit']:>10,.2f} {row['Profit_Margin']:>6.2f}% {int(row['Orders']):>7} ${row['Avg_Order_Value']:>10,.2f}")

# ANALYSIS 4: Regional Product Mix
print("\n" + "=" * 60)
print("🗺️  REGIONAL PRODUCT PREFERENCES")
print("=" * 60)

region_product = df.groupby(['Region', 'Product'])['Revenue'].sum().reset_index()
region_product = region_product.sort_values(['Region', 'Revenue'], ascending=[True, False])

for region in df['Region'].unique():
    region_data = region_product[region_product['Region'] == region].head(3)
    print(f"\n{region} Region - Top 3 Products:")
    for i, row in enumerate(region_data.itertuples(), 1):
        print(f"   {i}. {row.Product:15s} ${row.Revenue:>10,.2f}")

# ANALYSIS 5: Day of Week Performance
print("\n" + "=" * 60)
print("📅 SALES BY DAY OF WEEK")
print("=" * 60)

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_perf = df.groupby('Day_of_Week')['Revenue'].agg(['sum', 'count', 'mean'])
day_perf = day_perf.reindex(day_order)
day_perf = day_perf.dropna()

print("\nAverage Revenue by Day:")
for day, row in day_perf.iterrows():
    bar = '█' * int(row['mean'] / 200)
    print(f"{day:10s} ${row['mean']:>8,.2f} {bar}")

# VISUALIZATION: Create a comprehensive dashboard
print("\n📊 Creating advanced visualizations...")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Advanced Sales Analytics Dashboard', fontsize=18, fontweight='bold')

# Chart 1: Monthly Revenue Trend
ax1 = axes[0, 0]
monthly_perf['sum'].plot(kind='bar', ax=ax1, color='#4ECDC4')
ax1.set_title('Revenue by Month', fontweight='bold', fontsize=14)
ax1.set_xlabel('Month', fontsize=11)
ax1.set_ylabel('Revenue ($)', fontsize=11)
ax1.tick_params(axis='x', rotation=45)
ax1.grid(axis='y', alpha=0.3)

# Chart 2: Quarterly Comparison
ax2 = axes[0, 1]
x = np.arange(len(quarterly))
width = 0.35
ax2.bar(x - width/2, quarterly['Revenue'], width, label='Revenue', color='#4ECDC4')
ax2.bar(x + width/2, quarterly['Profit'], width, label='Profit', color='#FF6B6B')
ax2.set_title('Quarterly Revenue vs Profit', fontweight='bold', fontsize=14)
ax2.set_xlabel('Quarter', fontsize=11)
ax2.set_ylabel('Amount ($)', fontsize=11)
ax2.set_xticks(x)
ax2.set_xticklabels([f'Q{i}' for i in quarterly.index])
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

# Chart 3: Product Profit Margin
ax3 = axes[1, 0]
colors_margin = ['#2ECC71' if x > 30 else '#F39C12' if x > 25 else '#E74C3C' 
                 for x in product_profit['Profit_Margin']]
product_profit['Profit_Margin'].plot(kind='barh', ax=ax3, color=colors_margin)
ax3.set_title('Product Profit Margins', fontweight='bold', fontsize=14)
ax3.set_xlabel('Profit Margin (%)', fontsize=11)
ax3.set_ylabel('Product', fontsize=11)
ax3.grid(axis='x', alpha=0.3)

# Chart 4: Day of Week Pattern
ax4 = axes[1, 1]
day_perf['mean'].plot(kind='line', marker='o', ax=ax4, color='#9B59B6', linewidth=2, markersize=8)
ax4.set_title('Average Revenue by Day of Week', fontweight='bold', fontsize=14)
ax4.set_xlabel('Day', fontsize=11)
ax4.set_ylabel('Avg Revenue ($)', fontsize=11)
ax4.tick_params(axis='x', rotation=45)
ax4.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('charts/advanced_dashboard.png', dpi=300, bbox_inches='tight')
print("   ✅ Saved: charts/advanced_dashboard.png")
plt.close()

# INSIGHTS SUMMARY
print("\n" + "=" * 60)
print("💡 KEY BUSINESS INSIGHTS")
print("=" * 60)

most_profitable_product = product_profit.index[0]
highest_margin_product = product_profit['Profit_Margin'].idxmax()
best_day = day_perf['mean'].idxmax()

print(f"\n1. 📈 Best performing month: {best_month}")
print(f"2. 💰 Most profitable product: {most_profitable_product}")
print(f"3. 💎 Highest margin product: {highest_margin_product} ({product_profit.loc[highest_margin_product, 'Profit_Margin']:.1f}%)")
print(f"4. 📅 Best day for sales: {best_day}")
print(f"5. 🎯 Overall profit margin: {(df['Profit'].sum() / df['Revenue'].sum() * 100):.2f}%")

print("\n✅ ADVANCED ANALYSIS COMPLETE!")
print("=" * 60)