"""
> 2. Write a program to draw line and scatter plots for random 100 x and y coordinates
"""
# Solution by Zeeshan Sarwar

from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
import seaborn as sns
from plotly import express as px

try:
    rand_x= np.random.randint(1,101,100) 
    rand_y= np.random.randint(1,101,100)     
    plot1 = px.scatter(rand_x, rand_y)
    plot2 = px.line(rand_x, rand_y)
    plot1.show()
    plot2.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")