import os
import numpy as np
import pandas as pd

path="C:/Users/John.Yin/Desktop/temp/" #Change path here

for subdir, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.csv'):
            print(os.path.join(file))
            df = pd.read_csv(path + file ,encoding='latin-1')
#             df = pd.read_csv(path + file ,encoding='latin-1',mangle_dupe_cols=False)
            da=df.rename(columns={'a': 'phone', 'b': 'phone','c': 'phone', 'd': 'phone'})
            da.to_csv(path + file)
            print('Column names are replaced')
#             print(da)
        else:
            print('No csv file exists')
