import glob
import json
import os

import pandas as pd
from lxml import etree

tag_dic = {}
prod_name = ''
file_name = ''


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def xml_traverse(root, xpath):
    tag_name = etree.QName(root).localname
    if xpath not in tag_dic:
        tag_dic[xpath] = {
            'tag': tag_name,
            'xpath': xpath,
            'mapped_xpath': '',
            'file_name': file_name,
            'prod': prod_name,
        }

    for child in root:
        if not (type(child) == etree._ProcessingInstruction) and not (type(child) == etree._Comment):
            xml_traverse(child, f'{xpath}/{etree.QName(child).localname}')


def process_xml():
    file_name = 'temp.xml'
    print(file_name)
    tree = etree.parse(file_name)
    root = tree.getroot()
    xml_traverse(root, etree.QName(root).localname)
    df = pd.DataFrame(tag_dic.values())
    df.to_excel('xpath.xlsx', index=False)


if __name__ == '__main__':
    process_xml()

import sys

import pandas as pd


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
