"""
> 2. Write a program to draw a violin plot of “species” against “sepal length” for a dataset given
in a url
[https://github.com/mwaskom/seaborn-data/blob/master/iris.csv]
"""
# Solution by Zeeshan Sarwar

from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
import seaborn as sns
from plotly import express as px

try:
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    print(df.head())
    sns.violinplot(x='species', y='sepal_length', data=df)
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")