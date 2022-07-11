""""
> 26. Write a Python program to how to add an extra column to an numpy array.
> Expected Output:
> [[ 10 20 30 100]
> [ 40 50 60 200]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

original_array = np.array([[10, 20, 30],[40, 50 ,60]])
column_to_add = np.array([100, 200])

try:
    print("\n----------------------------\n")
    print(f"Original array elements: \n{original_array}")
    print("\n----------------------------\n")
    output_array = np.c_[original_array, column_to_add]
    print(f"Expected Output : \n{output_array}")
    print("\n----------------------------\n")
except Exception as e:
    print("Error : ",e)
else:
    print(f"Executed successfully on {datetime.datetime.now()}")