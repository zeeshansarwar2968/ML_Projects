"""
> 11. Write a Python program to create bar plot from a DataFrame.
> Sample Data Frame:\
> a b c d e\
> 2 4,8,5,7,6\
> 4 2,3,4,2,6\
> 6 4,7,4,7,8\
> 8 2,6,4,8,6\
> 10 2,4,3,3,2
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('Barchart\data.csv', index_col=0)
    print(df)
    df.plot(kind='bar')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")