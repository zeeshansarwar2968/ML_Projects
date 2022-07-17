"""
Question 13. 
> Write a Python program to display the grid and draw line charts of the closing value of
> Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with
> linestyle -, width .5. and color blue.
> Date,Close
> 03-10-16,772.559998
> 04-10-16,776.429993
> 05-10-16,776.469971
> 06-10-16,776.859985
> 07-10-16,775.080017
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt


try:
    data = pd.read_csv('data.csv')
    plt.plot(data.Date, data.Close, linestyle = 'solid', linewidth =2, color = 'black')
    plt.grid(linestyle='--', color="g", linewidth=0.5)
    plt.xticks(data.Date)
    plt.xlabel('Date')
    plt.ylabel('Closing Value')
    plt.title('Alphabet Inc.')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")