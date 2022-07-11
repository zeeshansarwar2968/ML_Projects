"""
> 3. Write a Python program to create a null vector of size 10 and update sixth value to 11.
> [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
> Update sixth value to 11
> [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

try:
    null_vector = np.zeros(10)
    print(f"Original Vector : \n{null_vector}")
    null_vector[6] = 11
    print(f"Update sixth value to 11 : \n{null_vector}")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")