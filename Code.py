import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Load dataset
df = pd.read_csv('/content/Sample - Superstore.csv', encoding='latin1')

# Data Cleaning
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Basic Analysis
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)

# Profit by Category
category_profit = df.groupby('Category')['Profit'].sum()

# Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# Visualization
plt.figure()
region_sales.plot(kind='bar', title='Sales by Region')
plt.savefig('output/region_sales.png')

plt.figure()
category_profit.plot(kind='bar', title='Profit by Category')
plt.savefig('output/category_profit.png')

plt.figure()
monthly_sales.plot(title='Monthly Sales Trend')
plt.savefig('output/monthly_sales.png')

print("Analysis complete. Check output folder.")
