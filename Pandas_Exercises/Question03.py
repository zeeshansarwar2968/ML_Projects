"""
> 3. Write a Python program to add, subtract, multiple and divide two Pandas Series.\
> Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime


try:
    series_1 = pd.Series([2, 4, 6, 8, 10])
    series_2 = pd.Series([1, 3, 5, 7, 9])
    print(f"\n---------------------------------------\n")
    #print(f"Sample series 01 : \n{series_1}")
    #print(f"Sample series 02 : \n{series_2}")
    print(f"Sample series addition : \n{series_1+series_2}")
    print(f"Sample series subtraction : \n{series_1-series_2}")
    print(f"Sample series multiplication : \n{series_1*series_2}")
    print(f"Sample series division : \n{series_1/series_2}")
    print(f"\n---------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
