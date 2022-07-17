"""
> 8. Write a Python programming to display a bar chart of the popularity of programming
> Languages. Select the width of each bar and their positions.\
> Sample data:\
> Programming languages: Java, Python, PHP, JavaScript, C#, C++\
> Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
> 
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

try:
    languages_position = [i for i, _ in enumerate(languages)]
    width_values = [0.5, 0.7, 0.8, 1.0, 0.9, 0.8]
    y_position = [0,1,2,3,4,5]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticks(languages_position, languages)
    ax.bar(y_position, popularity, color='yellow', edgecolor='blue', width=width_values)
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    ax.minorticks_on()
    ax.set_xlabel('Languages')
    ax.set_ylabel('Popularity')
    ax.set_title('Popularity Comparison of Languages')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")