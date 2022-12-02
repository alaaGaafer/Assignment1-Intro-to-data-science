#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
energy = pd.read_excel(r'C:\Users\alaau\Downloads\Assignment\Energy Indicators.xls')
# removing header and footer
energy = energy[17:244]
#dropping first two columns
energy = energy.drop(energy.columns[[0, 1]], axis=1)
#renaming the columns
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', 'Renewable']
#replacing all ... with NaN
energy.replace('...',np.NaN, inplace=True)
#converting petajoules to gigajoules
energy["Energy Supply"] *= 1000000 
#removing the numbers beside countries
energy['Country'] = energy['Country'].str.replace('\d+', '')
#removing the paranthes and its content beside countries
energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
#renaming some countries
energy.replace('Republic of Korea','South Korea', inplace=True)
energy.replace('United States of America','United States', inplace=True)
energy.replace('United Kingdom of Great Britain and Northern Ireland','United Kingdom', inplace=True)
energy.replace('China, Hong Kong Special Administrative Region','Hong Kong', inplace=True)
energy.head(60)


# In[28]:


GDP = pd.read_csv(r'C:\Users\alaau\Downloads\Assignment\world_bank.csv', skiprows=4)
#renaming a column for the merge
GDP.rename(columns={'Country Name':'Country'}, inplace=True)
#renaming some countries
GDP.replace('Korea, Rep.','South Korea', inplace=True)
GDP.replace('Iran, Islamic Rep.','Iran', inplace=True)
GDP.replace('Hong Kong SAR, China','Hong Kong', inplace=True)
#joining energy and GDP
union = pd.merge(energy, GDP, on='Country', how='inner')
#dropping the columns except 2010:2015
union=union.drop(union.loc[:, '1960':'2009'].columns, axis = 1)
#turning the indices from numbers to countries
union=union.set_index('Country')
union.head(60)


# In[29]:


def AVG_func():
    #performing mean function on the years from 2010 to 2015
    averageGDP = union.iloc[:,6:12].mean(axis=1)
    #returning top 15 countries in terms of average GDP
    averageGDP=averageGDP.nlargest(n=15)
    #sorting in descending order
    averageGDP.sort_values(ascending=False)
    return averageGDP
AVG_func()


# In[30]:


def mean_energy():
    result = energy[['Energy Supply per Capita']].mean()
    return result
mean_energy()


# In[31]:


def min_renewable():
    min_value=energy['Renewable'].min()
    print("the min Renewable = ",min_value)
    countries=energy['Country'][energy[ energy['Renewable'] == energy['Renewable'].min() ].index]
    print(countries)
min_renewable()


# In[ ]:





# In[ ]:





# In[ ]:




