"""
> 2. Write a Python program to draw a line using given axis values with suitable label in the x axis
> , y axis and a title
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

x_values = list(range(10000))
y_values = [i*i for i in x_values]
try:
    plt.plot(x_values, y_values, color='blue', linewidth=2, linestyle='dotted')
    plt.xlabel('X-Values')
    plt.ylabel('Y-Values')
    plt.title('Non-Linear relationship between x and y values')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
