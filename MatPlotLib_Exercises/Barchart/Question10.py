"""
> 10. Write a Python program to create bar plot of scores by group and gender. Use multiple X
> values on the same chart for men and women.\
> Sample Data:\
> Means (men) = (22, 30, 35, 35, 26)\
> Means (women) = (25, 32, 30, 35, 29)
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

mean_men = [22, 30, 35, 35, 26]
mean_women = [25, 32, 30, 35, 29]

try:
    fig, ax = plt.subplots()
    index = np.arange(5)
    bar_width = 0.35
    opacity = 0.8
    fig1 = plt.bar(index, mean_men, bar_width,color='blue',label='Men')
    fig2 = plt.bar(index + bar_width, mean_women, bar_width,color='red',label='Women')
    plt.xlabel('Person')
    plt.ylabel('Scores')
    plt.title('Scores by Group & Gender')
    plt.xticks(index + bar_width/2, ('T1', 'T2', 'T3', 'T4', 'T5'))
    plt.legend()
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")