"""
Question 11. 
> Write a Python program to plot several lines with different format styles in one command
> using arrays.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(1, 20, 2)
y1 = np.linspace(5,40, 10)
x2 = np.arange(1, 30, 3)
y2 = np.linspace(20,70, 10)
x3 = np.arange(1, 40, 4)
y3 = np.linspace(15, 95, 10)

try:
    plt.plot(x1, y1, "^-", x2, y2, "bs-", x3, y3, "g-")
    plt.xlabel('X-Values')
    plt.ylabel('Y-Values')
    plt.title('Several Lines with different format styles')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")