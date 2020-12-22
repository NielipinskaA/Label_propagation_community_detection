import pandas as pd
import os

dir_name = 'contest_data/AS'
newdir_name = 'contest_data/poprawione'

for file_name in os.listdir(dir_name):
    df = pd.read_csv(dir_name + '/' + file_name,header=None)
    new_df = df.copy()
    new_df = new_df.iloc[:, 1]
    new_df = new_df.drop_duplicates(keep='first', inplace=False)
    clusters = new_df.tolist()
    df.iloc[:, 1] = df.iloc[:, 1].apply(lambda val: clusters.index(val) + 1)
    df.to_csv(newdir_name+'/'+file_name, index=False, header=None)
