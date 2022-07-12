"""
> 1. Write a Python program to create and display a one-dimensional array-like object containing an array of data 
using Pandas module.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime

try:
    Original_list = list(range(72,91))
    print(f"\n---------------------------------------\n")
    print(f"Original-list : {Original_list}")
    pandas_array = pd.array(Original_list)
    print(f"One-dimensional pandas array : {pandas_array}")
    print(f"\n---------------------------------------\n")
    
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
