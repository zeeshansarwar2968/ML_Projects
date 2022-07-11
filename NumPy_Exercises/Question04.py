"""
> 4. Write a Python program to reverse an array (first element becomes last).
> Original array:
> [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
> Reverse array:
> [37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime

try:
    d = np.linspace(12, 37, 38-12, dtype=np.int64)
    # d.shape = (3, 3)
    print(d)
    reverse_d = d[::-1]
    print(reverse_d)
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")