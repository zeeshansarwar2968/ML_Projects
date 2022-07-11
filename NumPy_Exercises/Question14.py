"""
> 14. Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or
> will return the sorted, unique values that are in only one (not both) of the input arrays.
> Array1: [ 0 10 20 40 60 80]
> Array2: [10, 30, 40, 50, 70]
> Unique values that are in only one (not both) of the input arrays:
> [ 0 20 30 50 60 70 80]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

def exclusive_values(array_data1, array_data2):
    return np.setxor1d(array_data1, array_data2)


try:
    array1 = np.array([0, 10, 20, 40, 60, 80])
    array2 = np.array([10, 30, 40, 50, 70])

    print("\n--------------------------------------\n")
    print(f"Array1 : {array1}")
    print(f"Array2 : {array2}")
    unique_array = np.setxor1d(array1, array2)
    print(f"Unique values that are in only one (not both) of the input arrays: \n{unique_array}")
    print("\n--------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")