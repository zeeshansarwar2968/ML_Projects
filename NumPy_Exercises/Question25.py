""""
> 25. Write a Python program to suppresses the use of scientific notation for small
> numbers in numpy array.
> Expected Output:
> Original array elements:
> [ 1.60000000e-10 1.60000000e+00 1.20000000e+03 2.35000000e-01]
> Print array values with precision 3:
> [ 0. 1.6 1200. 0.235]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

original_array = np.array([1.60000000e-10, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01])

try:
    print("\n----------------------------\n")
    print(f"Original array elements: \n{original_array}")
    print("\n----------------------------\n")
    np.set_printoptions(precision=3, suppress=True)
    print(f"Print array values with precision 3 : \n{original_array}")
    print("\n----------------------------\n")
except Exception as e:
    print("Error : ",e)
else:
    print(f"Executed successfully on {datetime.datetime.now()}")