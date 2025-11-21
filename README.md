# Sales Performance Analytics & Forecasting

A Python-based analytics system that analyzes sales data, tracks performance metrics, and forecasts future revenue.

## Overview

This project takes sales transactions and generates business insights - identifying top-performing regions and products, analyzing trends over time, and predicting future sales using machine learning.

## The Problem

Businesses need quick answers to questions like:
- Which regions are performing best?
- What products drive the most profit?
- How will next quarter look?
- Where should we invest more resources?

This project automates that analysis.

## Tech Stack

- **Python** - Core language
- **pandas** - Data manipulation
- **matplotlib** - Visualizations
- **scikit-learn** - Forecasting model
- **Excel** - Data storage

## Key Results

Analysis of 500 sales transactions revealed:

**Financial Performance:**
- Total revenue: $498,815
- Profit: $151,503 
- Margin: 30.4%

**Regional Breakdown:**
- East region leads: $137K (27.5% of total)
- Performance well-balanced across regions (22-27% range)

**Product Performance:**
- Laptops: highest revenue at $169K
- Tablets: best profit margin at 31.5%
- August: peak month with $72K

**Forecast:**
- Next 3 months projected: $187K
- Growth trend: +6.7%

## Project Structure

**Data Generation (`generate_data.py`)**  
Creates realistic sales data with products, regions, dates, and prices.

**Basic Analysis (`analyze_data.py`)**  
Calculates KPIs - revenue, profit, regional performance, product rankings.

**Visualizations (`create_charts.py`)**  
Generates bar charts, pie charts showing distribution and comparisons.

**Forecasting (`forecast_sales.py`)**  
Linear regression model trained on monthly trends to predict future sales.

**Advanced Analysis (`advanced_analysis.py`)**  
Deep dive: monthly patterns, quarterly breakdowns, day-of-week trends, profitability by product.

**Report Generation (`generate_report.py`)**  
Compiles findings into executive summary with insights and recommendations.

## How to Use

Install requirements:
```bash
pip install pandas numpy matplotlib scikit-learn openpyxl
```

Run scripts in sequence:
```bash
python generate_data.py       # Generate dataset
python analyze_data.py         # Run analysis
python create_charts.py        # Create visuals
python forecast_sales.py       # Build forecast
python advanced_analysis.py    # Deep analysis
python generate_report.py      # Generate report
```

## Output Files

All visualizations saved to `charts/` folder:
- Regional revenue comparison
- Product performance ranking
- Sales distribution
- 3-month forecast
- Comprehensive dashboard

Executive summary saved as `EXECUTIVE_SUMMARY.txt` with findings and recommendations.

## Key Insights

**Regional Strategy**  
East region outperforms others by 5%. Understanding what drives this performance could help replicate success in other regions.

**Product Optimization**  
Tablets show higher margins (31.5%) than Laptops despite lower volume. Opportunity to shift mix toward higher-margin products.

**Seasonal Patterns**  
August consistently peaks. Inventory and marketing should align with this pattern.

**Growth Trajectory**  
Positive momentum at +6.7% suggests current strategies are effective.

## Technical Approach

**Data Processing:**
- Grouped transactions by region, product, time period
- Calculated aggregates (sum, mean, percentages)
- Sorted for rankings and comparisons

**Forecasting Method:**
- Linear regression on monthly revenue data
- Trained on 10 months of history
- Projected 3 months forward
- Validated with R² scoring

**Visualization Strategy:**
- Bar charts for comparisons
- Pie chart for distribution
- Line graphs for trends
- Multi-panel dashboard for comprehensive view

## Possible Extensions

- Real-time dashboard with Streamlit
- Database integration (PostgreSQL)
- Advanced forecasting models (ARIMA, Prophet)
- Customer segmentation
- A/B testing framework
- Automated reporting

## Project Files
```
sales-analytics-project/
├── generate_data.py           
├── analyze_data.py            
├── create_charts.py           
├── forecast_sales.py          
├── advanced_analysis.py       
├── generate_report.py         
├── sales_data.xlsx            # 500 transaction records
├── EXECUTIVE_SUMMARY.txt      # Full analysis report
└── charts/                    # All visualizations
    ├── revenue_by_region.png
    ├── revenue_by_product.png
    ├── region_distribution.png
    ├── sales_forecast.png
    └── advanced_dashboard.png
```

## Contact

**Bala Mahendra Pothabathula**

- Email: bala29mahendra@gmail.com
- LinkedIn: [linkedin.com/in/bala-mp](https://linkedin.com/in/bala-mp)
- Location: Tampa, FL

## Notes

This project uses generated sample data for demonstration. The analytical approach and methodology apply to real business datasets.

The forecasting model shows 25% accuracy on this random data. With real data exhibiting actual seasonal patterns, accuracy would improve significantly.

---

*End-to-end sales analytics project demonstrating data processing, analysis, forecasting, and business reporting.*