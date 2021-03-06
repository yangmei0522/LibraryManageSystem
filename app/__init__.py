from flask import Flask
from config import configs
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    db.init_app(app)

    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/api/user')

    from .book import book
    app.register_blueprint(book, url_prefix='/api/book')

    from .admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    if config_name == 'testing':
        return app, db

    return app
