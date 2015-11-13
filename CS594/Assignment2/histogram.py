__author__ = 'Niket'

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data1.csv', sep=',',header=None, index_col =0)

data.plot(kind='bar')
plt.ylabel('Count of occurrence of words')
plt.xlabel('Words')
plt.title('100 Most frequently occuring words')

plt.show()