"""
> 4. Write a Python program to draw line charts of the financial data of Alphabet Inc. between
> October 3, 2016 to October 7, 2016.\
> Sample Financial data (fdata.csv):\
> Date,Open,High,Low,Close\
> 03-10-16,774.25,776.065002,769.5,772.559998\
> 04-10-16,776.030029,778.710022,772.890015,776.429993\
> 05-10-16,779.309998,782.070007,775.650024,776.469971\
> 06-10-16,779,780.47998,775.539978,776.859985\
> 07-10-16,779.659973,779.659973,770.75,775.080017
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('fdata.csv')
    print(df)
    df.plot()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Market')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")