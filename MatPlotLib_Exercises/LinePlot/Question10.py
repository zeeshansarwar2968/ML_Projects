"""
Question 10. 
> Write a Python program to plot quantities which have an x and y position.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt


x1_values = list(range(75))
y1_values = [i*i for i in x1_values]
x2_values = list(range(25,100))
y2_values = [3*i for i in x2_values]

try:
    plt.plot(x1_values, y1_values, 'b*', x2_values, y2_values, 'ro')
    plt.xlabel('X-Values')
    plt.ylabel('Y-Values')
    plt.title('Lines with legends, different widths and colors')
    plt.legend()
    print(plt.axis())
    plt.axis((0, 70, 0, 200))
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")