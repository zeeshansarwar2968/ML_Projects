"""
> 17. Write a Python program to change the data type of an array.
> Expected Output:
> [[ 2 4 6]
> [ 6 8 10]]
> Data type of the array x is: int32
> New Type: float64
> [[ 2. 4. 6.]
> [ 6. 8. 10.]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

original_array = np.array([[2, 4, 6], [6, 8, 10]])
try:
    print("\n---------------------------------\n")
    print(f"Expected Output: \n{original_array}")
    print(f"Data type of the array x is: {original_array.dtype}")
    new_array = original_array.astype(np.float64)
    print(f"New Type: {new_array.dtype}")
    print(f"New array : \n{new_array}")
    print("\n---------------------------------\n")
    
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")