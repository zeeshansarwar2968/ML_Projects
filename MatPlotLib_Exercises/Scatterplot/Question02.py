"""
> 2. Write a Python program to draw a scatter plot with empty circles taking a random distribution
> in X and Y and plotted against each other.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

X = np.random.randint(100, size=25)
Y = np.random.randint(100, size=25)

try:
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    ax.scatter(X, Y, edgecolor='green', marker='o',s=100, linewidths=2, facecolors='none')
    ax.set_title('Scatter Plot of random distributions X and Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
