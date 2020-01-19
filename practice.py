import json
import pandas as pd
import numpy as np
file2 = pd.read_json('world_bank_projects.json')
df = pd.DataFrame(file2)
df = df.replace('', np.nan)
print(df.head())
print(df.columns)
print(df.info)
print(df['countrycode'].value_counts())