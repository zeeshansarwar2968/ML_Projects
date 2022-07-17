"""
Question 14. 
> Write a Python program to display the grid and draw line charts of the closing value of
> Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with
> rendering with a larger grid (major grid) and a smaller grid (minor grid).Turn on the grid but turn
> off ticks.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt


try:
    data = pd.read_csv('data.csv')
    plt.plot(data.Date, data.Close, linestyle = 'solid', linewidth =2, color = 'black')
    plt.grid(which='minor', linestyle='-', color="red", linewidth=0.5)
    plt.grid(which='major', color='blue',linewidth=0.5, linestyle=':')
    plt.tick_params(which='both', top='off', left='off', right='off', bottom='off')
    plt.xlabel('Date')
    plt.ylabel('Closing Value')
    plt.title('Alphabet Inc.')
    # plt.legend()
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")