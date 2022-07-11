"""
2. Create a 3x3 matrix with values ranging from 2 to 10.
> Expected Output:
> [[ 2 3 4]
> [ 5 6 7]
> [ 8 9 10]]
"""
# Solution by Zeeshan Sarwar

import numpy as np
import datetime


"""
linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
Return evenly spaced numbers over a specified interval.
Returns `num` evenly spaced samples, calculated over the
interval [`start`, `stop`].
The endpoint of the interval can optionally be excluded.
"""
try:
    d = np.linspace(2, 10, 9, dtype=np.int64)
    d.shape = (3, 3)
    print(d)
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")

# print(help(np.linspace))