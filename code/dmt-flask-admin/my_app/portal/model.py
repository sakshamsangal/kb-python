from flask_admin.contrib.sqla import ModelView

from my_app import db


class MyModelView(ModelView):
    # form_columns = ('sak', 'name')
    can_edit = True
    page_size = 8
    column_display_pk = True

    # list_display_pk = True
    # column_searchable_list = ('sak', 'name')
    # column_filters = ['sak', 'name']
    # column_editable_list = ['name']

    def is_accessible(self):
        return True


class XpathMapView(ModelView):
    form_columns = ('pat', 'map_to', 'ct', 'priority')
    can_edit = True
    page_size = 8
    column_display_pk = True

    # list_display_pk = True
    # column_searchable_list = ('sak', 'name')
    # column_filters = ['sak', 'name']
    # column_editable_list = ['name']

    def is_accessible(self):
        return True


class TagMaster(db.Model):
    tag_name = db.Column(db.String(250), primary_key=True)
    map_tag = db.Column(db.String(250))
    rendered = db.Column(db.String(250))
    file_name = db.Column(db.String(250))
    prod_name = db.Column(db.String(250))
    file_size = db.Column(db.Integer)
    ct = db.Column(db.String(250))
    has_text = db.Column(db.String(250))


class TagCt(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    tag_name = db.Column(db.String(50))
    ct = db.Column(db.String(50))


class Processed(db.Model):
    prod_name = db.Column(db.String(50), primary_key=True)
    ct = db.Column(db.String(50))
    master_tag = db.Column(db.Integer, default=0)
    master_att = db.Column(db.Integer, default=0)
    master_xpath = db.Column(db.Integer, default=0)
    master_pc = db.Column(db.Integer, default=0)


class PcMaster(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    tag_name = db.Column(db.String(50))
    file_name = db.Column(db.String(50))
    prod_name = db.Column(db.String(50))
    ct = db.Column(db.String(50))


class DataDic(db.Model):
    feat = db.Column(db.String(100), primary_key=True)
    ct = db.Column(db.String(50))
    tag_name = db.Column(db.String(50))


class XpathMap(db.Model):
    pat = db.Column(db.String(100), primary_key=True)
    map_to = db.Column(db.String(50))
    ct = db.Column(db.String(50))
    priority = db.Column(db.Integer)


class MyException(db.Model):
    pat = db.Column(db.String(100), primary_key=True)
    comp = db.Column(db.String(50))
    styling = db.Column(db.String(50))
    feat = db.Column(db.String(50))
    comm = db.Column(db.String(50))
    overwrite_feat = db.Column(db.Integer)
    ct = db.Column(db.String(50))
    priority = db.Column(db.Integer)


class AttMaster(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    tag_name = db.Column(db.String(50))
    att_key = db.Column(db.String(50))
    att_val = db.Column(db.String(50))
    file_name = db.Column(db.String(50))
    prod_name = db.Column(db.String(50))
    ct = db.Column(db.String(50))


class PatFeat(db.Model):
    pat = db.Column(db.String(100), primary_key=True)
    feat = db.Column(db.String(50))
    priority = db.Column(db.Integer)


class Phase(db.Model):
    feat = db.Column(db.String(100), primary_key=True)
    alpha1 = db.Column(db.Integer)
    alpha2 = db.Column(db.Integer)
    filter_on_col = db.Column(db.String(50))
    ct = db.Column(db.String(50))


class CompStyle(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    comp = db.Column(db.String(50))
    h1_style = db.Column(db.String(50))
    h2_style = db.Column(db.String(50))
    text_style = db.Column(db.String(50))
    feat = db.Column(db.String(50))
