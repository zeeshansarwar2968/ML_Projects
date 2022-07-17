"""
> 12. Write a Python program to create bar plots with error bars on the same figure. 
> Sample Date:\
> Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824\
> Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

mean_velocity = [0.2474, 0.1235, 0.1737, 0.1824]
standard_deviation_velocity =[0.3314, 0.2278, 0.2836, 0.2645]

try:
    ind = np.arange(4)    
    # the width of the bars
    width = 0.35   
    plt.bar(ind, mean_velocity, width, yerr=standard_deviation_velocity, color='red')
    plt.ylabel('Values')
    plt.xlabel('Velocity')
    plt.title('Values by Velocity')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")