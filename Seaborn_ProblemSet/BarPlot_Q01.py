"""
> 1. Write a program to draw bar plot of sex against survived for a dataset given in the url
[https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv]
"""
# Solution by Zeeshan Sarwar

from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
import seaborn as sns
from plotly import express as px

try:
    sns.set(style='whitegrid')
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
    print(df.head())
    sns.barplot(x='sex', y='survived', data=df)
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
