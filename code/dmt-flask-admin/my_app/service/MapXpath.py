import os

import pandas as pd

from my_app.portal.model import XpathMap


def map_xpath_to_tag(loc, ct, file_name, sn):
    os.makedirs(f'{loc}/{ct}/excel/dm_sheet', exist_ok=True)
    df = pd.read_excel(f'{loc}/{ct}/excel/{file_name}.xlsx', sheet_name=sn)
    t = ('m_xpath', 'comp', 'style', 'feat', 'comment', 'phase')
    for i, x in enumerate(t):
        df.insert(i, x, '')
    df['m_xpath'] = df['Legacy Xpaths']
    ls = XpathMap.query.order_by(XpathMap.priority).all()
    for tu in ls:
        df['m_xpath'].replace(to_replace=tu.pat, value=tu.map_to, regex=True, inplace=True)
    df.to_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_xpath.xlsx', index=False)
    return True
