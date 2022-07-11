""""
> 23. Write a Python program to convert a NumPy array into Python list structure.
> Expected Output:
> Original array elements:
> [[0 1]
> [2 3]
> [4 5]]
> Array to list:
> [[0, 1], [2, 3], [4, 5]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

original_array = np.array([[0, 1], [2, 3], [4, 5]])

try:
    print("\n----------------------------\n")
    print(f"Original array elements: \n{original_array}")
    print("\n----------------------------\n")
    print(f"Array to list : \n{original_array.tolist()}")
    print("\n----------------------------\n")
except Exception as e:
    print("Error : ",e)
else:
    print(f"Executed successfully on {datetime.datetime.now()}")