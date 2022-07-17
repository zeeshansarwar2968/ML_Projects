"""
> 1. Write a program to draw a violin plot of sex against total_bill for a given dataset
[https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv]\
"""
# Solution by Zeeshan Sarwar

from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
import seaborn as sns
from plotly import express as px

try:
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
    print(df.head(5))
    sns.violinplot(x='sex', y='total_bill', data=df)
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")