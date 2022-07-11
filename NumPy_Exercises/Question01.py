"""
> 1. Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.
> Expected Output:
> Original List: [12.23, 13.32, 100, 36.32]
> One-dimensional numpy array: [ 12.23 13.32 100. 36.32]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

try:
    Original_list = [12.23, 13.32, 100, 36.32]
    print(f"Original-list : {Original_list}")
    numpy_array = np.array(Original_list)
    print(f"One-dimensional numpy array : {numpy_array}")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
# print(np.__version__)
# print(dir(np))