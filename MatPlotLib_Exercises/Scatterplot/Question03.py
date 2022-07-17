"""
> 3. Write a Python program to draw a scatter plot using random distributions to generate balls of
> different sizes.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

X = np.random.randint(1, 25, 50)
Y = np.random.randint(1, 25, 50)
colors = np.random.randint(1,10,50)
areas = np.random.randint(25,150,50)

try:
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    ax.scatter(X, Y, s=areas, c=colors, alpha=0.85)
    ax.set_title('Scatter Plot of random distributions X and Y to generate balls of different sizes')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
