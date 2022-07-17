""""
Question 15. 
> Write a Python program to create multiple plots.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

    
try:
    df = pd.read_csv('data.csv')
    plt.subplot(2, 2, 1)
    plt.plot(df.Date, df.Close, color='g')
    plt.subplot(2,2,2)
    plt.plot(df.Date, df.Close, color='b')
    plt.subplot(2,2,3)
    plt.pie([4, 1, 3, 2], labels=['Python', 'C#', 'Javascript', 'Java'],  colors=['r', 'b', 'g', 'c'])
    plt.subplot(2,2,4)
    df.Close.hist()
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")