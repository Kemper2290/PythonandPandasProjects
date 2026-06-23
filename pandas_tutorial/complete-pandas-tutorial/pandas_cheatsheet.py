import pandas as pd
import numpy as np


#create a simple DataFrame

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
                  columns = ["A","B","C"],
                  index = ["x","y","z","zz"])


print(df.head(),'\n')

print(df.tail(2),'\n')

#load data from csv
#coffee = pd.read_csv("./warmup-data/coffee.csv")

# Load data from parquet
#results = pd.read_parquet('./data/results.parquet')
#load data from excel
#olympics_data = pd.read_excel("./data/olympics-data.xlsx",sheet_name="results")

#access columns
print(df.columns,'\n')

# access index
print(df.index,'\n')
print(df.index.tolist(),'\n')

#general info about the dataframe
print(df.info(),'\n')


#statistical summary
print(df.describe(),'\n')

#number of inques values in each column
df.nunique()

#access unique values in a column
df['A']
df['A'].unique()

# shape and size of DataFrame

df.shape
df.size

#filter rows obased on conditions








