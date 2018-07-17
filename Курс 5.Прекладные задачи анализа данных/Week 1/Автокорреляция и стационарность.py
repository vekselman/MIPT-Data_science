# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:14:42 2017

@author: leoni
"""

import os
path = r"D:\MIPT Data Scientce\Курс 5.Прекладные задачи анализа данных\Week 1"
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
milk = pd.read_csv(path.decode('utf8') +'\monthly-milk-production.csv',
                   ';', index_col=['month'], 
                   parse_dates=['month'], dayfirst=True)
milk.head()
milk.plot()

milk[0]
import statsmodels.api as sm
sm.tsa.stattools.adfuller(milk.iloc[:,0])

import calendar
import datetime
dates = milk.index.to_datetime()
days = [calendar.monthrange(date.year,date.month)[1] for date in dates]
milk2 = [milk.iloc[i,0]/float(days[i]) for i in range(len(days))]
milk["div"] = milk2
milk2
fig = figure
plt.plot(x=milk.index,y=milk.div)
sm.tsa.stattools.adfuller(milk2)
sum(milk2)
