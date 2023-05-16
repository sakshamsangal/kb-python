from lxml import etree

from my_app import db
from my_app.portal.model import AttMaster
from my_app.service import master

ct = ''
att_dic = {}
file_name = ''
prod_name = ''
file_size = ''


def xml_traverse_att(root):
    tag_name = etree.QName(root).localname
    for key, val in root.attrib.items():
        key = etree.QName(key).localname
        my_id = f'{tag_name}_{key}'
        if my_id not in att_dic:
            att_dic[my_id] = {
                'id': my_id,
                'tag_name': tag_name,
                'att_key': key,
                'att_val': val,
                'file_name': file_name,
                'prod_name': prod_name,
                'ct': ct
            }

    for child in root:
        if type(child) == etree._Element:
            xml_traverse_att(child)


def process_master_att(loc, content_type, all_dir, products):
    global att_dic, file_name, prod_name, ct
    ct = content_type

    ls = []
    for root, f_name, p_name, f_size in master.get_xml_root(loc, content_type, all_dir, products):
        file_name = f_name
        prod_name = p_name
        xml_traverse_att(root)
        ls.append((prod_name, ct))

    db.engine.execute(AttMaster.__table__.insert().prefix_with("or ignore"), list(att_dic.values()))

    att_dic = {}
    return True

