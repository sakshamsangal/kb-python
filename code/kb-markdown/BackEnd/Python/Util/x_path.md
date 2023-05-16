```python
import pandas as pd

def m_xpath(loc, sn):
    df = pd.read_excel(loc, sheet_name=sn)

    ans = {}
    for index, row in df.iterrows():
        xpath = row['xpath']
        ls = xpath.split('/')
        print(ls)
        ans = form_json(ans, ls)
    dc_to_json_file(ans, 'data.json')
    return 'data.json'

```

```python
def m_xpath(content_type):
    # read excel sheet and convert it to data frame
    df = pd.read_excel(f'{content_type}.xlsx', sheet_name=content_type)
    df1 = pd.read_excel('tagmaster.xlsx', sheet_name=content_type)

    pd.insert(4, 'm_xpath', '')
    pd.insert(5, 'comp', '')
    pd.insert(6, 'style', '')
    pd.insert(7, 'phase', '')
    pd.insert(8, 'feat', '')

    for index, row in df.iterrows():
        xpath = row['Legacy Xpaths']
        ls = xpath.split('/')[1:]
        map_ls = []

        for i, x in enumerate(ls):
            try:
                y = df1.loc[df1.tag == x, 'map_tag'].values[0]
            except:
                print(x)
                sys.exit(0)
            if y != 'skip':
                map_ls.append(y)
        df.iat[index, 4] = '/'.join(map_ls)
        print(index)
    df.to_excel(f'{content_type}_out.xlsx', index=False)
```