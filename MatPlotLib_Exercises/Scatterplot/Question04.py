"""
> 4. Write a Python program to draw a scatter plot comparing two subject marks of Mathematics
> and Science. Use marks of 10 students.\
> Test Data:\
> math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]\
> science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]\
> marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

try:
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    ax.scatter(marks_range, science_marks, edgecolor='green', marker='o',s=100, linewidths=2, label='Science-Marks')
    ax.scatter(marks_range, math_marks, edgecolor='blue', marker='o',s=100, linewidths=2, label='Maths-Marks')
    ax.set_title('Marks Plot of Maths and Science')
    plt.xlabel('Marks Range')
    plt.ylabel('Marks Scored')
    plt.legend()
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
