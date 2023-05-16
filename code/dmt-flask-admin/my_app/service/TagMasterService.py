import re

from lxml import etree

from my_app import db
from my_app.portal.model import TagMaster, TagCt, Processed
from my_app.service import master

ct = ''
parent_dic = {}
temp = {}
tag_dic = {}
tag_ct = []
file_name = ''
prod_name = ''
file_size = ''
has_text_tag = {}


def xml_traverse(parent, root):
    tag_name = etree.QName(root).localname
    if tag_name not in tag_dic:
        tag_dic[tag_name] = {
            'tag_name': tag_name,
            'map_tag': 'skip',
            'rendered': 'yes',
            'file_name': file_name,
            'prod_name': prod_name,
            'file_size': file_size,
            'ct': ct,
            'has_text': 'no'
        }

    parent_dic[tag_name] = parent
    # print(len(root.text))
    pattern = '(\n|\s|\r)*'
    if root.text is not None and not re.fullmatch(pattern, root.text):
        has_text_tag[tag_name] = {
            '_tag_name': tag_name
        }

    if root.tail is not None and not re.fullmatch(pattern, root.tail):
        has_text_tag[parent_dic[tag_name]] = {
            '_tag_name': parent_dic[tag_name]
        }

    for child in root:
        if type(child) == etree._Element:
            xml_traverse(tag_name, child)


def process_master_tag(loc, content_type, all_dir, products):
    global tag_dic, file_name, prod_name, file_size, ct, temp
    ct = content_type

    ls = []
    for root, f_name, p_name, f_size in master.get_xml_root(loc, content_type, all_dir, products):
        file_name = f_name
        prod_name = p_name
        file_size = f_size
        xml_traverse('', root)
        ls.append((prod_name, ct))

    db.engine.execute(TagMaster.__table__.insert().prefix_with("or ignore"), list(tag_dic.values()))
    from sqlalchemy import bindparam
    stmt = TagMaster.__table__.update().where(TagMaster.tag_name == bindparam('_tag_name')).values({
        'has_text': 'yes'
    })
    db.engine.execute(stmt, list(has_text_tag.values()))

    db.engine.execute(TagCt.__table__.insert().prefix_with("or ignore"),
                      [
                          {
                              "id": dic['ct'] + '_' + dic['tag_name'],
                              "tag_name": dic['tag_name'],
                              "ct": dic['ct']
                          }
                          for dic in tag_dic.values()
                      ])
    db.engine.execute(Processed.__table__.insert().prefix_with("or ignore"),
                      [
                          {
                              "prod_name": dic['prod_name'],
                              "ct": dic['ct']
                          }
                          for dic in tag_dic.values()
                      ])

    return True

