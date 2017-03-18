from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
babel = Babel(default_locale='zh_Hans_CN', default_timezone='UTC')
