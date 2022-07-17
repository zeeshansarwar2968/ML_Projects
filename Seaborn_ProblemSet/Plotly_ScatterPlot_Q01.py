"""
> 1. Write a program to draw a scatter plot for random 1000 x and y coordinates
"""
# Solution by Zeeshan Sarwar

from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
import seaborn as sns
from plotly import express as px

try:
    rand_x= np.random.randint(1,1001,1000) 
    rand_y= np.random.randint(1,1001,1000) 
    plot = px.scatter(rand_x, rand_y)
    plot.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")