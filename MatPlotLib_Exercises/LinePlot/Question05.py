"""
Question 5. 
> Write a Python program to plot two or more lines on same plot with suitable legends of each
> line.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

x_values = list(range(10))
y1_values = [i*i for i in x_values]
y2_values = [i for i in x_values]
y3_values = [i*3 for i in x_values]

try:
    plt.plot(x_values, y1_values, color='blue', linewidth=2, linestyle='dotted')
    plt.plot(x_values, y2_values, color='green', linewidth=3, linestyle='solid')
    plt.plot(x_values, y3_values, color='red', linewidth=1, linestyle='solid')
    plt.xlabel('X-Values')
    plt.ylabel('Y-Values')
    plt.title('Lines with legends for each lines')
    plt.legend(['y1', 'y2', 'y3'])
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")