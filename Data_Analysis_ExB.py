#%%
import numpy as np # makes call name 'numpy' = 'np' for easy typing
import pandas as pd # makes call name 'pandas' = 'pd'
import matplotlib.pyplot as plt 
import scipy # added this to do density plot

# Read and store data
sales = pd.read_csv(r'C:\Users\isaac\OneDrive\Data Analysis with Python Cert\FreeCodeCamp-Pandas-Real-Life-Example-master\data\sales_data.csv',parse_dates=True) #


sales['Revenue_per_Age'] = sales['Revenue']/sales['Customer_Age']

print(sales['Revenue_per_Age'].head()) # .head() shows only first 5 and some info on data

# Looks screwed up on normal code. But if put one at a time on Juypiter it works
sales['Revenue_per_Age'].plot(kind='density', figsize=(14,6))
sales['Revenue_per_Age'].plot(kind='hist', figsize=(14,6))

sales['Calulated_Cost'] = sales['Order_Quantity']* sales['Unit_Cost']
sales['Calulated_Cost'].head() # To skim data
sales['Calulated_Cost'] != sales['Cost'].sum() # To check for anomolies

sales.plot(kind='scatter', x='Calulated_Cost',y='Profit',figsize=(6,6))

sales['Calulated_Revenue'] = sales['Cost'] + sales['Profit']
sales['Calulated_Revenue'] != sales['Revenue'].sum()

sales['Revenue'].plot(kind='hist',bins=100,figsize=(14,6))

sales['Unit_Price'].head()
sales['Unit_Price'] *= 1.03 # multiply itself by 1.03 for 3% increase in price
sales['Unit_Price'].head()  # to check

#Gets sales only fom Kentucksy
sales.loc[sales['State'] == 'Kentucky']

#Average of the sales by this age group
sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean()
# Records of both of these age groups
sales.loc[(sales['Age_Group'] == 'Youth (<25)') | (sales['Age_Group'] == 'Adults (35-64)')].shape[0]
#Mean rev of sales of this age group in USA
sales.loc[(sales['Age_Group'] == 'Adults (35-64)') & (sales['Country'] == 'United States'), 'Revenue'].mean()

#increase Reve from France by 10%
sales.loc[(sales['Country'] == 'France'), 'Revenue'] *= 1.1  
# %%
