from collections import defaultdict

from lxml import etree

from my_app import db
from my_app.portal.model import PcMaster
from my_app.service import master

pc_dic = {}
ct = ''
file_name = ''
prod_name = ''


def xml_traverse_pc(root):
    my_ls = []
    for child in root:
        if type(child) == etree._Element:
            child_name = etree.QName(child).localname
            my_ls.append(child_name)
            xml_traverse_pc(child)
    tag_name = etree.QName(root).localname

    counter = defaultdict(int)
    for letter in my_ls:
        counter[letter] += 1
    my_id = tag_name + '=>'
    for k, v in counter.items():
        my_id += '_' + k + str(v)

    pc_dic[my_id] = {
        'id': my_id,
        'tag_name': tag_name,
        'file_name': file_name,
        'prod_name': prod_name,
        'ct': ct
    }


def process_master_pc(loc, content_type, all_dir, products):
    global pc_dic, file_name, prod_name, ct
    ct = content_type
    ls = []
    for root, f_name, p_name, f_size in master.get_xml_root(loc, content_type, all_dir, products):
        file_name = f_name
        prod_name = p_name
        xml_traverse_pc(root)
        ls.append((prod_name, ct))

    db.engine.execute(PcMaster.__table__.insert().prefix_with("or ignore"), list(pc_dic.values()))

    pc_dic = {}
    return True
