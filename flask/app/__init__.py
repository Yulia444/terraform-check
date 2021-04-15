from flask import Flask
from flask.helpers import get_debug_flag
from app.config import DevConfig, ProdConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_ckeditor import CKEditor
from flask_mail import Mail


app = Flask(__name__)
CONFIG = DevConfig if get_debug_flag() else ProdConfig
app.config.from_object(CONFIG)
ckeditor = CKEditor(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)
mail = Mail(app)

from app import views
from app.models import Image, Dish, Review, News
from app import admin