"""
> 7. Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
> Checkerboard pattern:
> [[0 1 0 1 0 1 0 1]
> [1 0 1 0 1 0 1 0]
> [0 1 0 1 0 1 0 1]
> [1 0 1 0 1 0 1 0]
> [0 1 0 1 0 1 0 1]
> [1 0 1 0 1 0 1 0]
> [0 1 0 1 0 1 0 1]
> [1 0 1 0 1 0 1 0]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import  datetime

def checkerboard_pattern(data_array):
    """_summary_

    Args:
        data_array (_type_): _description_

    Returns:
        _type_: _description_
    """
    temp = data_array.copy()
    temp[1::2, ::2] = 1
    temp[::2, 1::2] = 1
    return temp

try:
    base_array = np.zeros((8,8), dtype=int)
    print(base_array)
    final_array_1 = checkerboard_pattern(base_array)
    print(final_array_1)
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")