"""
> 7. Write a Python programming to display a bar chart of the popularity of programming
> Languages. Specify the position of each bar plot.\
> Sample data:\
> Programming languages: Java, Python, PHP, JavaScript, C#, C++\
> Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
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
    y_position = [0,1,2,4,6,9]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticks(languages_position, languages)
    ax.bar(y_position, popularity, color='yellow', edgecolor='blue', linewidth=3)
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    ax.minorticks_on()
    # ax.set_xticks(languages_position, languages)
    ax.set_xlabel('Languages')
    ax.set_ylabel('Popularity')
    ax.set_title('Popularity Comparison of Languages')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")