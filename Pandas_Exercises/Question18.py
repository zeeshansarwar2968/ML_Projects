"""
> 18. Write a Python program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
> exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
> 'Laura', 'Kevin', 'Jonas'],
> 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
> 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
> 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
> labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
> Values for each column will be:
> name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"
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
    pandas_data.loc['k'] = ['Suresh', 15.5, 1, 'yes']
    print(f"The DataFrame sorted by 'name' in descending order : \n{pandas_data.sort_values('name', ascending=False)}")
    print(f"\n---------------------------------------\n")
    print(f"The DataFrame sorted by 'score' in ascending order : \n{pandas_data.sort_values('score')}")
    print(f"\n---------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")