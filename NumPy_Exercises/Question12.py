"""
> 12. Write a Python program to find common values between two arrays.
> Expected Output:
> Array1: [ 0 10 20 40 60]
> Array2: [10, 30, 40]
> Common values between two arrays:
> [10 40]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

def common_values(array_data1, array_data2):
    return np.intersect1d(array_data1, array_data2)


try:
    array1 = np.array([0, 10, 20, 40, 60])
    array2 = np.array([10, 30, 40])
    print("\n--------------------------------------\n")
    print(f"Array1 : {array1}")
    print(f"Array2 : {array2}")
    common_array = common_values(array1, array2)
    print(f"Common values between two arrays: \n{common_array}")
    print("\n--------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")