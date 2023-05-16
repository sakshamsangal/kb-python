import pandas as pd

from my_app.portal.model import TagMaster, XpathMap


def map_tag(loc, ct1):
    df = pd.read_excel(f'{loc}/{ct1}/excel/dm_sheet/{ct1}_xpath.xlsx', sheet_name='Sheet1')
    ls = TagMaster.query.order_by(TagMaster.tag_name).all()

    for tu in ls:
        df['m_xpath'].replace(to_replace='/' + tu.tag_name + '/', value='/' + tu.map_tag + '/', regex=True, inplace=True)
        df['m_xpath'].replace(to_replace='/' + tu.tag_name + '$', value='/' + tu.map_tag, regex=True, inplace=True)

    ls = XpathMap.query.filter_by(ct='gen').order_by(XpathMap.priority).all()
    for tu in ls:
        df['m_xpath'].replace(to_replace=tu.pat, value=tu.map_to, regex=True, inplace=True)

    df.to_excel(f'{loc}/{ct1}/excel/dm_sheet/{ct1}_tag.xlsx', index=False)
    return True

