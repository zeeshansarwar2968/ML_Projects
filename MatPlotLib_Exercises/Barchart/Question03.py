"""
> 3. Write a Python programming to display a bar chart of the popularity of programming
> Languages. Use uniform color.\
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
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(languages, popularity, color='red', linewidth=3)
    ax.set_xlabel('Languages')
    ax.set_ylabel('Popularity')
    ax.set_title('Popularity Comparison of Languages')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")

