# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:36:47 2020

@author: fbinsayeed1
"""
import yahoo_fin.stock_info as si 
import matplotlib.pyplot as plt 
import datetime   
import numpy as np

company = 'AAPL' 

income_statement = si.get_income_statement(company, yearly = True) 

x_axis = []
for col in income_statement:
    col = str(col) 
    year = datetime.datetime.strptime(col, '%Y-%m-%d %H:%M:%S') 
    x_axis.append(year.strftime("%Y") ) 

x = np.array(x_axis[::-1]) 

revenue = (income_statement.loc['totalRevenue'])/1000000000
ebit = (income_statement.loc['ebit'])/1000000000 
gross_profit = (income_statement.loc['grossProfit'])/1000000000 
net_income = (income_statement.loc['netIncome'])/1000000000 

plt.plot(x,revenue[::-1], '.r-', label = 'Revenue')
plt.plot(x,gross_profit[::-1], marker = 'o', color ='b', label = 'Gross profit') 
plt.plot(x,ebit[::-1], marker = 'o', color = 'y', label = 'EBIT') 
plt.plot(x,net_income[::-1], marker = 'o', color = 'g', label = 'Net Income') 

    
plt.title("Historical Financial Summary")   
plt.legend() 
plt.ylabel('In Billions') 
plt.xlabel('Year') 
plt.show() 
