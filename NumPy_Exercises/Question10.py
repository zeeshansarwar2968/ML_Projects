"""
> 10. Write a Python program to find the real and imaginary parts of an array of complex
> numbers.
> Expected Output:
> Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
> Real part of the array:
> [ 1. 0.70710678]
> Imaginary part of the array:
> [ 0. 0.70710678]
"""
import numpy as np
import  datetime

try:
    Original_array = np.array([ 1.00000000+0.j, 0.70710678+0.70710678j])
    print("\n-----------------------------------------------\n")
    print("The original array is : ",Original_array)
    print(f"The real parts of the array are : {Original_array.real}")
    print(f"The imaginary parts of the array are : {Original_array.imag}")
    print("\n-----------------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")