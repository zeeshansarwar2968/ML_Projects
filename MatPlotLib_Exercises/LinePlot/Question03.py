"""
> 3. Write a Python program to draw a line using given axis values taken from a text file, with
> suitable label in the x axis, y axis and a title.
> Test Data:
> test.txt
> 1 2
> 2 4
> 3 1
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

try:
    x = np.loadtxt('test.txt', delimiter=' ')
    df = pd.DataFrame(x)
    df.plot(x=0,y=1)
    plt.xlabel('X-Values')
    plt.ylabel('Y-Values')
    plt.title('Relationship between provided values')
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
