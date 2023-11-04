import json

import pandas as pd

d = {}
df = None
map = {}


def foo(parent, child, xpath):
    global map
    if isinstance(parent, dict):
        if map[xpath]['dt'] == "obj":
            if child not in parent:
                parent[child] = {}
        elif map[xpath]['dt'] == "str":
            parent[child] = map[xpath]['ex']
        elif map[xpath]['dt'] == "listOfObj":
            if child not in parent:
                parent[child] = [{}]
            return parent[child][0]
        elif map[xpath]['dt'] == "listOfStr":
            parent[child] = [map[xpath]['ex']]
            return parent[child]
    elif isinstance(parent, list):
        if map[xpath]['dt'] == "str":
            parent[0][child] = map[xpath]['ex']
            return parent[0]
    return parent[child]
    # return child


def sak(x):
    temp = d
    q = ''
    for child in x:
        q = q + '/' + child
        temp = foo(temp, child, q)


def m_xpath(loc, sn):
    global df, map
    df = pd.read_excel(loc, sheet_name=sn)

    x = df.set_index("xpath", drop=True)
    map = x.to_dict(orient="index")
    # print(map)

    # filter
    df = df[df['remark'] == 'm']
    for index, row in df.iterrows():
        xpath = row['xpath']
        ls = xpath.split('/')[1:]
        # print(ls)
        sak(ls)


def dc_to_json_file(dc, fn='data.json'):
    with open(fn, 'w') as outfile:
        # sort_keys = True
        j = json.dumps(dc, indent=4)
        outfile.write(j)


if __name__ == '__main__':
    m_xpath('xpath.xlsx', 'Sheet1')
    dc_to_json_file(d, 'out.json')
