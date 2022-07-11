""""
> 24. Write a Python program to convert a NumPy array into Python list structure.
> Expected Output:
> Original array elements:
> [ 0.26153123 0.52760141 0.5718299 0.5927067 0.7831874 0.69746349
> 0.35399976 0.99469633 0.0694458 0.54711478]
> Print array values with precision 3:
> [ 0.262 0.528 0.572 0.593 0.783 0.697 0.354 0.995 0.069 0.547]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

original_array = np.array([ 0.26153123, 0.52760141, 0.5718299, 0.5927067, 0.7831874, 0.69746349, 0.35399976, 0.99469633, 0.0694458, 0.54711478])

try:
    print("\n----------------------------\n")
    print(f"Original array elements: \n{original_array}")
    print("\n----------------------------\n")
    print(f"Print array values with precision 3 : \n{[round(i, 3) for i in original_array.tolist()]}")
    print("\n----------------------------\n")
except Exception as e:
    print("Error : ",e)
else:
    print(f"Executed successfully on {datetime.datetime.now()}")