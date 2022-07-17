"""
> 3. Write a program to draw a scatter plot for random 500 x and y coordinates and style it
"""
# Solution by Zeeshan Sarwar

from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
import seaborn as sns
from plotly import express as px

try:
    rand_x= np.random.randint(1,501,500) 
    rand_y= np.random.randint(1,501,500)     
    plot = px.scatter(x=rand_x,y=rand_y, color=rand_y, size=rand_x)
    plot.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")