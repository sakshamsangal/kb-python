import json

import pandas as pd

ans = []


def dfs(d, xpath):
    for k, v in d.items():
        if isinstance(v, dict):
            xp = xpath + "/" + k
            ans.append((xp, 'obj', '', 'o'))
            dfs(v, xpath + '/' + k)
        elif isinstance(v, list):
            for c, i in enumerate(v):
                if isinstance(i, dict):
                    xp = xpath + "/" + k
                    ans.append((xp, 'listOfObj', '', 'o'))
                    dfs(i, xpath + "/" + k)
                if isinstance(i, str):
                    xp = xpath + "/" + k
                    ans.append((xp, 'listOfStr', i, 'o'))
        else:
            xp = xpath + "/" + k
            ans.append((xp, 'str', v, 'm'))


# Opening JSON file
with open('in.json') as json_file:
    data = json.load(json_file)
    dfs(data, "")
    df = pd.DataFrame(ans, columns=['xpath', 'dt', 'ex', 'remark'])
    df.drop_duplicates(inplace=True, subset=["xpath"], keep='first')
    # df.drop_duplicates(keep='first', inplace=True)
    df.to_excel('xpath.xlsx', index=False)
    # df.to_csv('xpath.csv', index=False)
