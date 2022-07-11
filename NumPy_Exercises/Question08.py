"""
> 8. Write a Python program to convert a list and tuple into arrays.
> List to array:
> [1 2 3 4 5 6 7 8]
> Tuple to array:
> [[8 4 6]
> [1 2 3]]
> 
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

def to_array(array_data):
    """_summary_

    Args:
        array_data (_type_): _description_
    """
    return np.array(array_data)

try:
    list_data = [i for i in range(1,9)]
    list_to_array = to_array(list_data)
    print(f"List to Array conversion : {list_to_array} and type of data : {type(list_to_array)} and shape of data : {list_to_array.shape}")
    tuple_data = ([8, 4, 6], [1, 2, 3])
    tuple_to_array = to_array(tuple_data)
    print(f"Tuple to Array conversion : {tuple_to_array} and type of data : {type(tuple_to_array)} and shape of data : {tuple_to_array.shape}")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")