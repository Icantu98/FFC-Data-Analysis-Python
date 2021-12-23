#%%
import numpy as np # makes call name 'numpy' = 'np' for easy typing
import pandas as pd # makes call name 'pandas' = 'pd'
import matplotlib.pyplot as plt 
import scipy # added this to do density plot

##### PUT AN r INFRONT OF STRING TO MAKE IT A RAW STRING ####
sales = pd.read_csv(r'C:\Users\isaac\OneDrive\Data Analysis with Python Cert\FreeCodeCamp-Pandas-Real-Life-Example-master\data\sales_data.csv',parse_dates=True) #

print(sales.head()) # shows first few rows
print(sales.shape) # Return a tuple representing the dimensionality of the DataFrame.
print(sales.info()) # Concise summary of a DataFrame.
print(sales.describe()) # Generate various summary statistics

print(sales['Unit_Cost'].describe()) # Gives Stats for 'Unit_Cost'
print(sales['Unit_Cost'].mean())
print(sales['Unit_Cost'].median(),"\n")
#print(sales['Unit_Cost'])

# These are the different types of plots
'''
‘line’ : line plot (default)
‘bar’ : vertical bar plot
‘barh’ : horizontal bar plot
‘hist’ : histogram
‘box’ : boxplot
‘kde’ : Kernel Density Estimation plot
‘density’ : same as ‘kde’
‘area’ : area plot
‘pie’ : pie plot
‘scatter’ : scatter plot
‘hexbin’ : hexbin plot
'''
# I dont know how to make seperate figures yet so there are isssues when overwritng data on the plot

'''
# Sets up the settings of the plot
sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))
# shows the plot 
#plt.show() 

# Sets up a density plot
sales['Unit_Cost'].plot(kind='density',figsize=(14,6))
#plt.show() # might take few seconds to load if there are multiple plots

ax = sales['Unit_Cost'].plot(kind='density',figsize=(14,6))
ax.axvline(sales['Unit_Cost'].mean(), color ='red')
ax.axvline(sales['Unit_Cost'].median(), color ='green')
#plt.show()

ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6))
ax.set_ylable('Number of Sales')
ax.set_xlable('Dollars')
'''

print(sales['Age_Group'].value_counts())
sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))

axx = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14,6))

# Correlation Plot
corr = sales.corr()

fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()

# Scatter plot
sales.plot(kind='scatter', x='Customer_Age',y='Revenue', figsize=(6,6))
sales.plot(kind='scatter', x='Revenue',y='Profit', figsize=(6,6))

# Box plots Profit vs Agegroup
ax = sales[['Profit','Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
ax.set_ylable('Profit')

boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost','Unit_Price','Profit']
sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))
# %%
