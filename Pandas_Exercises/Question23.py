""""
> 23. Write a Python program to get list from DataFrame column headers.
> Sample data:
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
> 'Laura', 'Kevin', 'Jonas'],
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
"""
# Solution by Zeeshan Sarwar

import numpy as np
import pandas as pd
import datetime

exam_data = {
            'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
            'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
            }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

try:
    print(f"\n---------------------------------------\n")
    pandas_data = pd.DataFrame(exam_data, labels)
    print(f"The list from DataFrame column headers : \n{pandas_data.columns.to_list()}")
    print(f"The list from DataFrame column index : \n{pandas_data.index.to_list()}")
    print(f"\n---------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")