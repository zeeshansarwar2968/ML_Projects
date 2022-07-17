"""
> 1. Write a Python program to draw a line with suitable label in the x axis, 
y axis and a title
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

x= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

try:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='blue', linewidth=3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('A simple Linear curve')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
