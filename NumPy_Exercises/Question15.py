""""
> 15. Write a Python program compare two arrays using numpy.
> Array a: [1 2]
> Array b: [4 5]
> a > b
> [False False]
> a >= b
> [False False]
> a < b
> [ True True]
> a <= b
> [ True True] 
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

try:
    array_a = np.array([1, 2])
    array_b = np.array([4, 5])
    print("\n----------------------------------\n")
    print(f"Array a : {array_a}")
    print(f"Array b : {array_b}")
    print(f"a > b : \n{array_a > array_b}")
    print(f"a >= b : \n{array_a >= array_b}")
    print(f"a < b : \n{array_a < array_b}")
    print(f"a <= b : \n{array_a <= array_b}")
    print("\n----------------------------------\n")
    
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
    
    
    
