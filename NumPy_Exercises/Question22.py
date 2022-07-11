"""
> 22. Write a Python program to create an array of (3, 4) shape, multiply every element
> value by 3 and display the new array.
> Expected Output:
> Original array elements:
> [[ 0 1 2 3]
> [ 4 5 6 7]
> [ 8 9 10 11]]
> New array elements:
> [[ 0 3 6 9]
> [12 15 18 21]
> [24 27 30 33]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

try:
    original_array = np.array(list(range(12)))
    original_array = original_array.reshape(3,4) 
    print("\n---------------------------------\n")
    print(f"Original array elements : \n{original_array}")
    print("\n---------------------------------\n")
    multiplied_array = original_array * 3
    print(f"New array elements : \n{multiplied_array}")
    print("\n---------------------------------\n")
except Exception as e:
    print("Error : ",e)
else:
    print(f"Executed successfully on {datetime.datetime.now()}")