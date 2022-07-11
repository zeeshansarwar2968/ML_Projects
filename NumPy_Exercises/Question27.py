""""
> 27. Write a Python program to remove specific elements in a numpy array.
> Expected Output:
> Original array:
> [ 10 20 30 40 50 60 70 80 90 100]
> Delete first, fourth and fifth elements:
> [ 20 30 60 70 80 90 100]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

original_array = np.linspace(10, 100, 10, dtype=int)

try:
    print("\n----------------------------\n")
    print(f"Original array: \n{original_array}")
    print("\n----------------------------\n")
    output_array = np.delete(original_array, [0, 3, 4])
    print(f"Delete first, fourth and fifth elements : \n{output_array}")
    print("\n----------------------------\n")
except Exception as e:
    print("Error : ",e)
else:
    print(f"Executed successfully on {datetime.datetime.now()}")