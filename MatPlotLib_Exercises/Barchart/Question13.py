"""
> 13.  Write a Python program to create bar plots with errorbars on the same figure. Attach a text
> label above each bar displaying men means (integer value).\
> Sample Data\
> Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824\
> Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import patches as ptch

mean_velocity = [0.2474, 0.1235, 0.1737, 0.1824]
standard_deviation_velocity =[0.3314, 0.2278, 0.2836, 0.2645]

try:
    ind = np.arange(4)  
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, mean_velocity, width, color='blue', yerr=standard_deviation_velocity)
    plt.ylabel('Values')
    plt.xlabel('Velocity')
    plt.title('Velocity Values')
    val_patch = ptch.Patch(color='red', label='Mean')
    plt.legend(handles=[val_patch])
    for rect in rects1:
       height = rect.get_height()
       ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' %height, ha='center', va='bottom')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")