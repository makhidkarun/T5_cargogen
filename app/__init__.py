'''T5_cargogen app/__init__.py'''

import logging
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config


LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    # format='%(asctime)-15s %(name)s %(funcName)s(): %(message)s',
    format='%(relativeCreated)d %(name)s %(funcName)s(): %(message)s',
    level=logging.INFO
)

bootstrap = Bootstrap()


def create_app(config_name):
    '''Create app'''
    LOGGER.debug('Setting up app %s', __name__)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
