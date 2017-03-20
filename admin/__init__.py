from flask_admin import Admin
from fo.models import Registration
from .views import UserRegisterView
from fo.extensions import db


def create_admin(app):
    admin = Admin(
        app, url='/admin', template_mode='bootstrap3'
    )

    admin.add_view(UserRegisterView(
        Registration, db.session, '报名用户', endpoint='register'))

    return admin
