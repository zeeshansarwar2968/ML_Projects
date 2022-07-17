""""
> 2. Write a program to draw swarm plot of “total bill” against day for a dataset given in url
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
    sns.swarmplot(x='day',y='total_bill', data=df)
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")