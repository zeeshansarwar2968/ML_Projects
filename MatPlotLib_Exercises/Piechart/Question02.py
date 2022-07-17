"""
> 2. Write a Python programming to create a pie chart with a title of the popularity of programming
> Languages.\
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
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    ax.pie(popularity, labels=languages, autopct='%1.1f%%')
    ax.set_title('Popularity of Programming Languages')
    plt.legend()
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
