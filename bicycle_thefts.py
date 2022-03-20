import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data exploration
# Load the data
df_bicycle_thefts = pd.read_csv("Bicycle_Thefts.csv")

# Basic exploration: data types, description, statistics, samples
print(df_bicycle_thefts.info())
print(df_bicycle_thefts.describe())
print(df_bicycle_thefts.sample(5))

# Missing data evaluation
missing_values_count = df_bicycle_thefts.isnull().sum()
print(missing_values_count)

# Data visualization
sns.histplot(df_bicycle_thefts['Status'])
#
