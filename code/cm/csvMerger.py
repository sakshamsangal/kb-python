import glob
import os

import pandas as pd


def view():
    ls = []
    for name in glob.glob(f'*.csv'):
        x = os.path.basename(name)
        df = pd.read_csv(x)
        df = df[df['b'] > 20]
        # df = df[df['b'].str.contains("")]
        ls.append(df)

    df_concat = pd.concat(ls, ignore_index=True)
    df_concat.to_csv('out.csv', index=False)


if __name__ == '__main__':
    view()
