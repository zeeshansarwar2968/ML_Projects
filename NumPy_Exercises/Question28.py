""""
> 28. Write a Python program to save a NumPy array to a text file.
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

original_array = np.linspace(10, 1000, 25, dtype=int)

try:
    print("\n----------------------------\n")
    print(f"Original array: \n{original_array}")
    print("\n----------------------------\n")
    output_array = np.reshape(original_array, (5,5))
    print(f"Output Array : \n{output_array}")
    print("\n----------------------------\n")
    np.savetxt("q28_output.txt",output_array, delimiter=" ", header="Question 28 Solution Array")
except Exception as e:
    print("Error : ",e)
else:
    print(f"Executed successfully on {datetime.datetime.now()}")