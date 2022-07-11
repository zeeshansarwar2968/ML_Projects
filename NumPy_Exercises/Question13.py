"""
> 13. Write a Python program to find the set difference of two arrays. The set difference
> will return the sorted, unique values in array1 that are not in array2.
> Expected Output:
> Array1: [ 0 10 20 40 60 80]
> Array2: [10, 30, 40, 50, 70, 90]
> Set difference between two arrays: [ 0 20 60 80]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

def diff_values(array_data1, array_data2):
    return np.setdiff1d(array_data1, array_data2)


try:
    array1 = np.array([0, 10, 20, 40, 60, 80])
    array2 = np.array([10, 30, 40, 50, 70, 90])

    print("\n--------------------------------------\n")
    print(f"Array1 : {array1}")
    print(f"Array2 : {array2}")
    common_array = diff_values(array1, array2)
    print(f"Set difference between two arrays: {common_array}")
    print("\n--------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")