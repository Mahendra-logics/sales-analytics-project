# Sales Forecasting - Predict future revenue!
# This uses machine learning to predict next 3 months

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

print("🔮 SALES FORECASTING SYSTEM")
print("=" * 60)

# Load data
df = pd.read_excel('sales_data.xlsx')
df['Date'] = pd.to_datetime(df['Date'])

# STEP 1: Aggregate sales by month
print("\n📊 Analyzing monthly trends...")

df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('YearMonth')['Revenue'].sum().reset_index()
monthly_sales['Month_Num'] = range(1, len(monthly_sales) + 1)

print(f"✅ Analyzed {len(monthly_sales)} months of data")

# STEP 2: Prepare data for machine learning
# X = Month number (1, 2, 3, 4...)
# y = Revenue for that month

X = monthly_sales['Month_Num'].values.reshape(-1, 1)
y = monthly_sales['Revenue'].values

# STEP 3: Train the forecasting model
print("\n🤖 Training forecasting model...")

model = LinearRegression()
model.fit(X, y)

# Calculate accuracy
predictions = model.predict(X)
accuracy = model.score(X, y) * 100

print(f"✅ Model trained successfully!")
print(f"📈 Model Accuracy: {accuracy:.2f}%")

# STEP 4: Predict next 3 months
print("\n" + "=" * 60)
print("🔮 SALES FORECAST - NEXT 3 MONTHS")
print("=" * 60)

last_month_num = monthly_sales['Month_Num'].max()
future_months = np.array([[last_month_num + 1], 
                          [last_month_num + 2], 
                          [last_month_num + 3]])

future_predictions = model.predict(future_months)

# Get dates for future months
last_date = df['Date'].max()
future_dates = []
for i in range(1, 4):
    next_date = last_date + timedelta(days=30 * i)
    future_dates.append(next_date.strftime('%B %Y'))

print("\nPredicted Revenue:")
for i, (date, revenue) in enumerate(zip(future_dates, future_predictions), 1):
    print(f"   {i}. {date:15s}  ${revenue:>12,.2f}")

total_predicted = future_predictions.sum()
print(f"\n💰 Total Predicted (3 months): ${total_predicted:,.2f}")

# STEP 5: Calculate growth rate
current_total = monthly_sales['Revenue'].tail(3).sum()
growth = ((total_predicted - current_total) / current_total) * 100

print(f"📈 Projected Growth: {growth:+.2f}%")

# STEP 6: Create visualization
print("\n📊 Creating forecast visualization...")

plt.figure(figsize=(14, 7))

# Plot historical data
plt.plot(monthly_sales['Month_Num'], monthly_sales['Revenue'], 
         marker='o', linewidth=2, markersize=8, label='Actual Sales', color='#4ECDC4')

# Plot trend line (what model learned)
plt.plot(monthly_sales['Month_Num'], predictions, 
         linestyle='--', linewidth=2, label='Trend', color='#FF6B6B', alpha=0.7)

# Plot future predictions
future_x = [last_month_num + 1, last_month_num + 2, last_month_num + 3]
plt.plot(future_x, future_predictions, 
         marker='s', markersize=10, linewidth=2, label='Forecast', 
         color='#FFA07A', linestyle='--')

# Add labels to forecast points
for x, y, date in zip(future_x, future_predictions, future_dates):
    plt.text(x, y, f'\n${y:,.0f}', ha='center', fontweight='bold', fontsize=10)

plt.title('Sales Forecast - Historical & Predicted', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Create output folder
import os
os.makedirs('charts', exist_ok=True)

plt.tight_layout()
plt.savefig('charts/sales_forecast.png', dpi=300, bbox_inches='tight')
print("   ✅ Saved: charts/sales_forecast.png")
plt.close()

# STEP 7: Forecast by Region
print("\n" + "=" * 60)
print("🗺️  REGIONAL FORECASTS")
print("=" * 60)

for region in df['Region'].unique():
    region_df = df[df['Region'] == region]
    region_monthly = region_df.groupby('YearMonth')['Revenue'].sum().reset_index()
    region_monthly['Month_Num'] = range(1, len(region_monthly) + 1)
    
    X_region = region_monthly['Month_Num'].values.reshape(-1, 1)
    y_region = region_monthly['Revenue'].values
    
    model_region = LinearRegression()
    model_region.fit(X_region, y_region)
    
    next_month_pred = model_region.predict([[len(region_monthly) + 1]])[0]
    
    print(f"\n{region:10s} → Next month predicted: ${next_month_pred:>12,.2f}")

print("\n" + "=" * 60)
print("✅ FORECASTING COMPLETE!")
print("=" * 60)

# Summary
print("\n📋 SUMMARY:")
print(f"   • Historical months analyzed: {len(monthly_sales)}")
print(f"   • Model accuracy: {accuracy:.2f}%")
print(f"   • Forecast period: 3 months")
print(f"   • Projected revenue: ${total_predicted:,.2f}")
print(f"   • Growth trend: {growth:+.2f}%")