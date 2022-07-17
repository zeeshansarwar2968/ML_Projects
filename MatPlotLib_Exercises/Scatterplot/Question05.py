"""
> 5. Write a Python program to draw a scatter plot for three different groups camparing weights
> and heights.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

weight_values_01=[67,57.2,59.6,59.64,55.8,61.2,60.45,61,56.23,56]
height_values_01=[101.7,197.6,98.3,125.1,113.7,157.7,136,148.9,125.3,114.9]
weight_values_02=[61.9,64,62.1,64.2,62.3,65.4,62.4,61.4,62.5,63.6]
height_values_02=[152.8,155.3,135.1,125.2,151.3,135,182.2,195.9,165.1,125.1]
weight_values_03=[68.2,67.2,68.4,68.7,71,71.3,70.8,70,71.1,71.7]
height_values_03=[165.8,170.9,192.8,135.4,161.4,136.1,167.1,235.1,181.1,177.3]

try:
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    ax.scatter(height_values_01, weight_values_01, edgecolor='green', marker='o',s=100, linewidths=2, label='Group-01')
    ax.scatter(height_values_02, weight_values_02, edgecolor='blue', marker='o',s=100, linewidths=2, label='Group-02')
    ax.scatter(height_values_03, weight_values_03, edgecolor='red', marker='o',s=100, linewidths=2, label='Group-03')
    ax.set_title('Weight and Height Comparison')
    plt.xlabel('Height Range(in cms)')
    plt.ylabel('Weight Range(in KGs)')
    plt.legend()
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")