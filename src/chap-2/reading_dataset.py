from typing import Callable
import os

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
  data = pd.read_csv(csv_path)
  print(data['NumRooms'][1])

def run():
  if not os.path.exists(csv_path):
    generate_csv()
  read_csv()

run()
