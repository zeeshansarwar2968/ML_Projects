"""
> 6. Write a Python program to add a border (filled with 0's) around an existing array.
> Expected Output:
> Original array:
> [[ 1. 1. 1.]
> [ 1. 1. 1.]
> [ 1. 1. 1.]]
> 1 on the border and 0 inside in the array
> [[ 0. 0. 0. 0. 0.]
> [ 0. 1. 1. 1. 0.]
> [ 0. 1. 1. 1. 0.]
> [ 0. 1. 1. 1. 0.]
> [ 0. 0. 0. 0. 0.]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime


# method 01
def add_borders_1(array_data):
    """
    1 on the border and 0 inside in the array
    Args:
        array_data (_type_): ndArray of order nxm
    """
    output_array = np.resize(array_data, (5, 5))
    output_array[0:-1, 0] = 0
    output_array[0:-1, -1] = 0
    output_array[0,:] = 0
    output_array[-1,:] = 0
    return output_array
    

# method 02
def add_borders_2(array_data):
    """
    1 on the border and 0 inside in the array
    Args:
        array_data (_type_): ndArray of order nxm
    """
    return np.pad(array_data, pad_width=1, mode="constant", constant_values=0)


try:
    original_array = np.ones((3,3), dtype=float)
    print(f"\n----------------------------------------------\n")
    print(f"add_borders_method_01 : \n{add_borders_1(original_array)}")
    print(f"\n----------------------------------------------\n")
    print(f"add_borders_method_02 : \n{add_borders_2(original_array)}")
    print(f"\n----------------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")

