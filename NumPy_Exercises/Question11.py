"""
> 11. Write a Python program to find the number of elements of an array, length of one
> array element in bytes and total bytes consumed by the elements.
> Expected Output:
> Size of the array: 3
> Length of one array element in bytes: 8
> Total bytes consumed by the elements of the array: 24
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

try:
    demo_list = list(range(101,104))
    original_array = np.array(demo_list, dtype=np.float64)
    print("\n------------------------------------------\n")
    print("Size of the array: ", original_array.size)
    print("Length of one array element in bytes: ", original_array.itemsize)
    print("Total bytes consumed by the elements of the array: ", original_array.nbytes)
    print("\n------------------------------------------\n")
except Exception as e:
    print("Error : ",e)
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
