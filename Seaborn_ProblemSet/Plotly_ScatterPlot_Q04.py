"""
> 4. Write a program to draw a scatter plot for a given dataset and show datalabels on hover
https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv
"""
# Solution by Zeeshan Sarwar

from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
import seaborn as sns
from plotly import express as px


try:
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
    print(df.head(20))
    plot = px.scatter(df,x='State', y='Population', color="State", hover_data=list(df.columns))
    plot.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")