"""
> 4. Write a Python program to get the powers of an array values element-wise.
> Note: First array elements raised to powers from second array
> Expected Output:
> Original array
> [0 1 2 3 4 5 6]
> First array elements raised to powers from second array, element-wise:
> [ 0 1 8 27 64 125 216]
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime


try:
    array_1 = [0, 1, 2, 3, 4, 5, 6]
    array_2 = [3, 3, 3, 3, 3, 3, 3]
    print(f"\n---------------------------------------\n")
    print(f"Sample array 01 : \n{array_1}")
    print(f"Sample array 02 : \n{array_2}")
    output_array = [array_1[i]**array_2[i] for i in range(len(array_1))]
    pandas_data = pd.DataFrame(output_array)
    print(f"First array elements raised to powers from second array, element-wise: : \n{pandas_data}")
    print(f"\n---------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")