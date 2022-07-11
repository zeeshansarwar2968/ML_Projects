"""
> 20. Write a Python program to concatenate two 2-dimensional arrays.
> Expected Output:
> Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
> Expected Output:
> [[ 0 1 3 0 2 4]
> [ 5 7 9 6 8 10]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

array_a = np.array([[0, 1, 3], [5, 7, 9]])
array_b = np.array([[0, 2, 4], [6, 8, 10]])

try:
    print("\n----------------------------\n")
    print(f"Sample arrays: {array_a.tolist(), array_b.tolist()}")
    print("\n----------------------------\n")
    output_array_1 = np.concatenate([array_a, array_b], axis=0)
    print(f"Expected Output 1 with axis 0 : \n{output_array_1}")
    output_array_2 = np.concatenate([array_a, array_b], axis=1)
    print(f"Expected Output 2 with axis 1 : \n{output_array_2}")
    print("\n----------------------------\n")
except Exception as e:
    print("Error : ",e)
else:
    print(f"Executed successfully on {datetime.datetime.now()}")