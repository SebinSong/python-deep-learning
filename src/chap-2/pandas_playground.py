import numpy as np
import pandas as pd

## 1. Series
s = pd.Series(range(0, 10, 2), index=['a', 'b', 'c', 'd', 'e'], name='col1')

# Using iloc[] - integer-location based indexing.
s1 = s.iloc[:3] # -> slicng
v1 = s.iloc[1] # gets the value

# Getting dtype
dt = s.dtype

# get/set actions on Series using index label (Similar to how dict works)
s['a'] += 10

got1 = s['b']
got2 = s.get('f', 77) # using .get method, it's possible to set the default vallue.

# Vectorized operations
s2 = s + 50 # s ** 2, s / 10 etc...
s3 = np.exp(s) # dtype of s3 now becomes float64

# Cloning a series with a different name
s4 = s.rename('col2') 

# Creating dataframe from multiple series
df0 = pd.DataFrame(s)
df0.insert(1, s4.name, s4)

## 2. Dataframe
# - is a 2-Dimensional labeled data structure with columns of potentially different types.
# - Term 'index' refers to the label of each row.

# Creating a dataframe with a dict of series

# - keys of dict will be column names
# - Column orders are kept
# - indexes are the union of the indexes of the passed series, if not passed explicitly.
d = {
  'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
  'two': pd.Series([10, 20, 30, 40], index=['b', 'c', 'd', 'e'])
}

df = pd.DataFrame(d)

# explicitly specifying the dataframe indexes
# NOTE: index orders are kept
df2 = pd.DataFrame(d, index=['d', 'c', 'b'])

# Getting column labels and indexes
col_labels = df.columns
row_indexes = df.index

# From dict of ndarrays
d2 = {
  'first_col': [1, 2, 3, 4, 5],
  'second_col': [-1, -2, -3, -4, -5] 
}
df2 = pd.DataFrame(d2, index=list('abcde')) # could pass index list eg: pd.Dataframe(d, index=['r1', 'r2', 'r3', ...])

# Column selection
col_first = df2['first_col']

# Deriving a new column from existing ones
df2['col_third'] = df2['second_col'] * 10

# Creating a new column with a default value
df2['flag'] = True

# Deleting a column
del df2['flag']


# Adding a column with a series
df2['col_series'] = s4

# Selecting a dataframe row by label
row1 = df2.loc['b']
row2 = df2.iloc[1] # by integer location

# Slicing dataframe rows
sliced_df = df2[1:4]

# Dataframe can be generated using numpy ndarray
df3 = pd.DataFrame(
  np.random.randn(10, 4) * 100,
  columns=['col1', 'col2', 'col3', 'col4'],
  index=list('abcdefghij')
)

df4 = pd.DataFrame(
  np.random.randn(7, 3) * 1000,
  columns=['col2', 'col3', 'col4'],
  index=list('cdefghj')
)

df5 = df3 + df4

df5 /= 100 # Arithmetic operations with scalars are applied element-wise.

# Transposing a dataframe
transposed_df3 = df3[:5].T

# Getting numpy ndarray from DataFrame.
# NOTE: This is useful when turning DataFrame instance to a Pytorch tensor
# eg.) torch.tensor(df.values, dtype=torch.float64) - dtype here is used to convert elements.
ndarr = transposed_df3.values
print(ndarr)
