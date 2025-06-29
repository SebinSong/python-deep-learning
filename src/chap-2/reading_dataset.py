from typing import Callable
import os
import torch

# reference - Basic data structures in pandas (Series, Dataframe)
# https://pandas.pydata.org/docs/user_guide/dsintro.html

# helper functions
# reference: http://docs.python.org/3.13/library/os.path.html#os.path.normpath
curr_dir_path = os.path.dirname(__file__)
resolve_path: Callable[[str], str] = lambda relPath: os.path.normpath(os.path.join(curr_dir_path, relPath))
data_dir_path = resolve_path('../../data')
csv_path = os.path.join(data_dir_path, 'house_tiny.csv')

def generate_csv():
  if not os.path.isdir(data_dir_path):
    os.makedirs(data_dir_path)

  with open(csv_path, 'w') as f:
    f.write('NumRooms,Alley,Price\n') # column names
    f.write('NA,Pave,127500\n') # Each row represents a data example
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

def read_csv():
  import pandas as pd
  # NOTE: pd.read_csv reads the csv file as pandas DataFrame instance.
  data = pd.read_csv(csv_path)

  # Lets populate the missing data here!
  # inputs here is another Data frame, outputs here is a Series
  inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]

  first_input = inputs['NumRooms'] # select a column as a Series

  # use Series.fillna(), Series.mean() methods
  inputs['NumRooms'] = first_input.fillna(first_input.mean())

  inputs = pd.get_dummies(inputs, columns=['Alley'], dtype=int) # dtype=int here converts True/False to 1 and 0.

  tensor_inputs = torch.tensor(inputs.values, dtype=torch.int32) # dtype parameter here is used to convert the elements.
  tensor_outputs = torch.tensor(outputs.values, dtype=torch.float32)
  print(tensor_inputs)
  print(tensor_outputs)

def run():
  if not os.path.exists(csv_path):
    generate_csv()
  read_csv()

# run()

def run2 ():
  csv_path = os.path.join(data_dir_path, 'random_csv.csv')

  if not os.path.exists(csv_path): return False

  with open(csv_path) as f:
    from math import isnan
    import pandas as pd

    # Helper lambdas
    _isnan: Callable[[any], bool] = lambda x: isinstance(x, float) and isnan(x)
    sum_ascii = lambda s: sum(ord(c) for c in s)

    # loads csv data as a pandas dataframe
    data = pd.read_csv(csv_path)
    most_nan = ('', 0)

    for col_name in data.columns:
      nans = [1 for el in data[col_name].values if _isnan(el)]
      
      if len(nans) >= most_nan[1]:
        most_nan = (col_name, len(nans))
    
      random_val = next((a for a in data[col_name].values if not _isnan(a)), 'abcd1234')

      # in-place application of sum_ascii function.
      data[col_name][:] = data[col_name].fillna(random_val).apply(sum_ascii) # Series.apply

    print(most_nan)
    del data[most_nan[0]]

    data_tensor = torch.from_numpy(data.values.astype(int))  # DataFrame.values returns a numpy ndarray of the dataframe table.
    print(data_tensor)

run2()
