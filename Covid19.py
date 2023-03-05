
import numpy as np;
import scipy as sp;
import matplotlib.pyplot as plt;
import seaborn as sns;
import requests;
import pandas as pd;
import sklearn;
from sklearn import linear_model;
import math;
import random;
import sqlite3;
import pyodbc ;
import networkx as nx;
from mpl_toolkits.mplot3d import axes3d;
from matplotlib import style;
import matplotlib.animation as animation;
import pyodbc;
import sys;
import statistics;
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_log_error;
from sklearn.model_selection import train_test_split;
import yfinance as yf;
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score;
from sklearn import metrics;
import plotly.graph_objects as go
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.graphics.tsaplots import plot_acf
import pickle
pd.options.mode.chained_assignment = None  # default='warn'
sns.set()
import yfinance as yf
import json
from pandas_datareader import data as pdr
import datetime
 
data=pd.read_csv('/Users/lindritdemelezi/Covid19/owid-covid-data.csv')



data.index=data.date
data['date']=data['date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%d-%m') if x != "" else "")
print(data.head())
test=pd.read_csv('/Users/lindritdemelezi/Covid19/test.csv')

'''
print(train.head())

print(train.pivot_table(columns='Country_Region',values='ConfirmedCases'))
filtrimi=train.groupby(['Country_Region'])['Fatalities'].sum()
top10=pd.DataFrame(filtrimi)
sortimi=top10.sort_values(by='Fatalities',ascending=False)
print(sortimi.iloc[0:10])
figura=sortimi.iloc[0:10].plot(kind='bar')
plt.bar_label(figura.containers[0])
plt.show()
'''
data1=data[data['location']=='Kosovo']

#print(data1.columns)

print(data1[['location','date','new_cases','new_deaths','total_deaths','new_tests','new_vaccinations','people_vaccinated','people_fully_vaccinated','population']])
data1.dropna()
ax=data1['new_deaths'].tail(30).plot(kind='bar')
plt.bar_label(ax.containers[0],rotation=90)
plt.xlabel('Data')
plt.ylabel('Numri i vdekjeve ne Kosove')
plt.show()
ax=data1['new_cases'].tail(30).plot(kind='bar')
plt.bar_label(ax.containers[0],rotation=90)
plt.xlabel('Data')
plt.ylabel('Numri i rasteve te reja ne Kosove')
plt.show()
#print(data1.new_tests.sum())
data2=data1[data1['date']=='2021-09-17']
data3=pd.DataFrame(data2)

print(data3[['new_cases']])