"""
> 19. Write a Python program to create an array which looks like below array.
> Expected Output:
> [[ 0. 0. 0.]
> [ 1. 0. 0.]
> [ 1. 1. 0.]
> [ 1. 1. 1.]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

try:
    demo_array = np.zeros((4,3))
    count = 1
    while count<len(demo_array):
        demo_array[count,:count] = 1
        count +=1    
    print(f"\n--------------------------------------\n")
    print(f"Expected Output 1 : \n{demo_array}")
    print(f"\n--------------------------------------\n")
    print(f"Expected Output 2 : \n{np.tri(4, 3, -1)}")
    print(f"\n--------------------------------------\n")    
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")