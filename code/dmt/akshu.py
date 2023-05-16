import re

import pandas as pd


df_p = pd.read_excel('akshu_p.xlsx', sheet_name='pat')
df = pd.read_excel('akshu.xlsx', sheet_name='Sheet1')

for index1, row1 in df_p.iterrows():
    for index, row in df.iterrows():
        if pd.isnull(df.loc[index, 'comp']):
            print(row1['pat'], row['xpath'])
            pat = re.compile(row1['pat'])
            if re.fullmatch(pat, row['xpath']):
                df.iat[index, 2] = row1['comp']
                df.iat[index, 3] = row1['style']

df.to_excel('akshu.xlsx', index=False)


