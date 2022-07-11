"""
> 5. Write a Python program to create a 2d array with 1 on the border and 0 inside.
> Expected Output:
> Original array:
> [[ 1. 1. 1. 1. 1.]
> [ 1. 1. 1. 1. 1.]
> [ 1. 1. 1. 1. 1.]
> [ 1. 1. 1. 1. 1.]
> [ 1. 1. 1. 1. 1.]]
> 1 on the border and 0 inside in the array
> [[ 1. 1. 1. 1. 1.]
> [ 1. 0. 0. 0. 1.]
> [ 1. 0. 0. 0. 1.]
> [ 1. 0. 0. 0. 1.]
> [ 1. 1. 1. 1. 1.]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

try:
    original_array = np.full((5,5), 1, dtype=float)
    output_array = original_array.copy()
    output_array[1:-1, 1:-1] = 0
    print(f"Original array : \n{original_array}")
    print(f"1 on the border and 0 inside in the array : \n{output_array}")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")