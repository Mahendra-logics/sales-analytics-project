# Executive Summary Report Generator
# Creates a professional text report of all findings

import pandas as pd
from datetime import datetime

print("📄 Generating Executive Summary Report...")

# Load data
df = pd.read_excel('sales_data.xlsx')
df['Date'] = pd.to_datetime(df['Date'])

# Calculate all metrics
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_revenue) * 100
total_orders = len(df)
avg_order = df['Revenue'].mean()
if 'Customer_ID' in df.columns:
    unique_customers = df['Customer_ID'].nunique()
else:
    unique_customers = total_orders  # Assume 1 customer per order

# Regional performance
region_sales = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
best_region = region_sales.index[0]

# Product performance
product_sales = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
best_product = product_sales.index[0]

# Monthly performance
df['Month_Name'] = df['Date'].dt.month_name()
monthly = df.groupby('Month_Name')['Revenue'].sum()
best_month = monthly.idxmax()

# Create the report
report = f"""
{'='*70}
                   SALES PERFORMANCE EXECUTIVE SUMMARY
{'='*70}

Report Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
Analysis Period: {df['Date'].min().strftime('%B %Y')} - {df['Date'].max().strftime('%B %Y')}

{'='*70}
                        KEY PERFORMANCE INDICATORS
{'='*70}

Financial Performance:
   • Total Revenue:              ${total_revenue:>15,.2f}
   • Total Profit:               ${total_profit:>15,.2f}
   • Profit Margin:              {profit_margin:>15.2f}%
   • Average Order Value:        ${avg_order:>15,.2f}

Sales Volume:
   • Total Orders:               {total_orders:>15,}
   • Average Orders per Day:     {total_orders / len(df['Date'].unique()):>15.1f}

{'='*70}
                         REGIONAL PERFORMANCE
{'='*70}

Revenue by Region:
"""

for region, revenue in region_sales.items():
    pct = (revenue / total_revenue) * 100
    report += f"   • {region:10s}  ${revenue:>12,.2f}  ({pct:>5.1f}% of total)\n"

report += f"\n🏆 Top Performing Region: {best_region}\n"

report += f"""
{'='*70}
                         PRODUCT PERFORMANCE
{'='*70}

Top 5 Products by Revenue:
"""

for i, (product, revenue) in enumerate(product_sales.head(5).items(), 1):
    report += f"   {i}. {product:15s}  ${revenue:>12,.2f}\n"

report += f"\n🏆 Best Selling Product: {best_product}\n"

# Product profitability
product_profit = df.groupby('Product').agg({
    'Profit': 'sum',
    'Revenue': 'sum'
})
product_profit['Margin'] = (product_profit['Profit'] / product_profit['Revenue']) * 100
highest_margin = product_profit['Margin'].idxmax()

report += f"💎 Highest Profit Margin: {highest_margin} ({product_profit.loc[highest_margin, 'Margin']:.1f}%)\n"

report += f"""
{'='*70}
                        TEMPORAL ANALYSIS
{'='*70}

Best Performing Month: {best_month} (${monthly[best_month]:,.2f})

Quarterly Breakdown:
"""

quarterly = df.groupby(df['Date'].dt.quarter).agg({
    'Revenue': 'sum',
    'Profit': 'sum'
})

for quarter, row in quarterly.iterrows():
    margin = (row['Profit'] / row['Revenue']) * 100
    report += f"   Q{quarter}: Revenue ${row['Revenue']:>12,.2f}  |  Profit ${row['Profit']:>12,.2f}  |  Margin {margin:.1f}%\n"

# Growth trend
monthly_sorted = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum().sort_index()
if len(monthly_sorted) > 1:
    first_month = monthly_sorted.iloc[0]
    last_month = monthly_sorted.iloc[-1]
    growth = ((last_month - first_month) / first_month) * 100
else:
    growth = 0

report += f"""
{'='*70}
                        KEY INSIGHTS & RECOMMENDATIONS
{'='*70}

Strategic Insights:

1. Regional Focus:
   → {best_region} region leads with {(region_sales[best_region] / total_revenue * 100):.1f}% of total revenue
   → Recommendation: Increase marketing investment in {best_region} region

2. Product Strategy:
   → {best_product} generates highest revenue (${product_sales[best_product]:,.2f})
   → {highest_margin} has best profit margin ({product_profit.loc[highest_margin, 'Margin']:.1f}%)
   → Recommendation: Expand {highest_margin} product line for better margins

3. Growth Trend:
   → {'Positive' if growth > 0 else 'Negative'} trend: {growth:+.1f}% growth from start to end period
   → Recommendation: {'Maintain current strategies' if growth > 0 else 'Review sales strategies'}

4. Operational Efficiency:
   → Profit margin of {profit_margin:.1f}% is {'healthy' if profit_margin > 25 else 'acceptable'}
   → Average order value: ${avg_order:.2f}
   → Recommendation: Focus on upselling to increase AOV

{'='*70}
                              CONCLUSION
{'='*70}

Overall Performance: {'STRONG' if profit_margin > 25 and growth > 0 else 'MODERATE'}

The sales data shows {"strong performance across all regions" if region_sales.std() < region_sales.mean() * 0.2 else "varied regional performance"}.
{best_product} and {highest_margin} are key revenue and profit drivers respectively.

Next Steps:
   1. Implement targeted campaigns in {best_region} region
   2. Increase inventory for {best_product}
   3. Optimize pricing for {highest_margin} to maximize margins
   4. Monitor monthly trends and adjust strategies quarterly

{'='*70}

Report prepared by: Sales Analytics System
Data source: sales_data.xlsx
Total records analyzed: {len(df):,}

{'='*70}
"""

# Save report
with open('EXECUTIVE_SUMMARY.txt', 'w', encoding='utf-8') as f:
    f.write(report)

print("✅ Executive Summary Report Generated!")
print("📄 Saved to: EXECUTIVE_SUMMARY.txt")

# Also print to console
print(report)