"""
> 3. Write a Python programming to create a pie chart of gold medal achievements of five most
> successful countries in 2016 Summer Olympics. Read the data from a csv file.
> Sample data:
> medal.csv
> country,gold_medal
> United States,46
> Great Britain,27
> China,26
> Russia,19
> Germany,17
"""
# Solution by Zeeshan Sarwar

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('Piechart\medal.csv')
    print(df)
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)
    ax.pie(df.gold_medal, labels= df.country, autopct='%1.1f%%')
    ax.set_title('2016 Summer Olympics')
    plt.legend()
    plt.show()
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Executed successfully on {datetime.datetime.now()}")
