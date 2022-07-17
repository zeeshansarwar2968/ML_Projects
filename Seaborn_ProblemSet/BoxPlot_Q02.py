"""
> 2. Write a program to draw a box plot of day by tips for a dataset given in a url
[https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv]
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
    sns.boxplot(x='day', y='tip', data=df)
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")