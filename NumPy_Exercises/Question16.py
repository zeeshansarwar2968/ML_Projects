"""
> 16. Write a Python program to create a contiguous flattened array.
> Original array:
> [[10 20 30]
> [20 40 50]]
> New flattened array:
> [10 20 30 20 40 50]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

original_array = np.array([[10, 20, 30], [20, 40, 50]])
try:
    print("\n---------------------------------\n")
    print(f"Original array : \n{original_array}")
    flattened_array = np.ravel(original_array, order='C')
    print(f"New Flattened array : \n{flattened_array}")
    print("\n---------------------------------\n")
    
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")