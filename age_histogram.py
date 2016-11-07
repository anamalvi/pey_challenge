import matplotlib.pyplot as plt
from numpy.random import normal
from numpy import genfromtxt
import pandas as pd

df = pd.read_csv('census_data/census_train.csv')
age = df.Age.tolist()

plt.hist(age, bins=30, normed=True)
plt.title("Age Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()