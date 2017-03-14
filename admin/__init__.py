from flask_admin import Admin
from flask_admin import AdminIndexView


def create_admin(app):
    admin = Admin(
        app, url='/admin', template_mode='bootstrap3'
    )
    return admin
