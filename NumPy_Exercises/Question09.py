""""
> 9. Write a Python program to append values to the end of an array.
> Expected Output:
> Original array:
> [10, 20, 30]
> After append values to the end of the array:
> [10 20 30 40 50 60 70 80 90]
"""

import numpy as np
import datetime

try:
    original_array = np.array([10, 20, 30])
    print("\n---------------------------------\n")
    print("Original array : \n",original_array)
    print("\n---------------------------------\n")
    final_array = np.append(original_array, [40, 50 ,60, 70, 80, 90])
    # original_array.append(np.array([40, 50, 60]))
    print("After append values to the end of the array: \n",final_array)
    print("\n---------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")