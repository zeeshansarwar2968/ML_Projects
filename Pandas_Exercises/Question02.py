"""
> 2. Write a Python program to convert a Panda module Series to Python list and it's type.
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime


try:
    Original_list = list(range(72,91))
    print(f"\n---------------------------------------\n")
    pandas_array = pd.Series(Original_list)
    print(f"Panda module Series : \n{pandas_array} and the type is : {type(pandas_array)}")
    converted_list = pandas_array.tolist()
    print(f"\nPython list : {converted_list} and the type is : {type(converted_list)}")
    
    print(f"\n---------------------------------------\n")
    
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
