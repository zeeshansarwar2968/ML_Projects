"""
> 18. Write a Python program to create a 3-D array with ones on a diagonal and zeros
> elsewhere.
> Expected Output:
> [[ 1. 0. 0.]
> [ 0. 1. 0.]
> [ 0. 0. 1.]]
"""
import numpy as np
import datetime


try:
    identity_array = np.eye(3)
    print("\n---------------------------------\n")
    print(f"Expected Output: \n{identity_array}")
    print("\n---------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")