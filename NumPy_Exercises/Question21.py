"""
21. Write a Python program to make an array immutable (read-only).
> Expected Output:
> Test the array is read-only or not:
> Try to change the value of the first element:
> Traceback (most recent call last):
> File "19236bd0-0bd9-11e7-a232-c706d0968eb6.py", line 6, in
> x[0] = 1
> ValueError: assignment destination is read-only
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

try:
    sample_array = np.array([21, 43, 13, 46])
    sample_array.flags.writeable = False
    print(f"Test the array is read-only or not : ")
    print(f"Try to change the value of the first element : ")
    sample_array[0] = 1
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")