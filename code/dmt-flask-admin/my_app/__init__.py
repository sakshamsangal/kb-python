import os

from flask_cors import CORS
from flask_admin import Admin

"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DFAULT_DB_URI = "sqlite:///dmt.db"
DB_URI = os.getenv('DB_URI', DFAULT_DB_URI)


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SECRET_KEY'] = 'akshu'
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    db.init_app(app)

    with app.app_context():
        # engine = create_engine('postgresql://postgres:postgres@localhost/user_info')

        from my_app.portal.model import TagMaster
        from my_app.portal.views import portal
        from my_app.portal.model import MyModelView
        from my_app.portal.model import XpathMapView
        from my_app.portal.model import TagCt
        from my_app.portal.model import Processed
        from my_app.portal.model import PcMaster, DataDic, XpathMap, MyException, AttMaster, PatFeat, Phase, CompStyle

        app.register_blueprint(portal)

        admin = Admin(app, name='DM Sheet filler', template_mode='bootstrap3')
        admin.add_view(MyModelView(DataDic, db.session))
        admin.add_view(XpathMapView(XpathMap, db.session))
        admin.add_view(MyModelView(TagMaster, db.session, category="Master"))
        admin.add_view(MyModelView(TagCt, db.session, category="Tag"))
        admin.add_view(MyModelView(Processed, db.session, category="Tag"))
        admin.add_view(MyModelView(PcMaster, db.session, category="Master"))
        admin.add_view(MyModelView(MyException, db.session))
        admin.add_view(MyModelView(AttMaster, db.session, category="Master"))
        admin.add_view(MyModelView(PatFeat, db.session))
        admin.add_view(MyModelView(CompStyle, db.session))
        admin.add_view(MyModelView(Phase, db.session))

        db.create_all()  # Create database tables for our data models

        return app
