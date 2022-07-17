"""
Question 12. 
> Write a Python program to create multiple types of charts
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
x4 = np.linspace(1, 60, 44)
y4 = np.arange(3, 90, 2)

try:
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
    ax1.plot(x1, y1,"g-")
    ax2.bar(x2, y2,color="blue")
    ax3.hist(y3,histtype='bar', color="lightblue")
    ax4.scatter(x1, y1,color="green")
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")