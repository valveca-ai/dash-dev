from flask import Flask
from dash import Dash

from .layouts import main_aqa_layout
from .cache import


def create_app(config_object=f'{__package__}.settings'):
    server = Flask(__package__)

    # load default settings
    server.config.from_object(config_object)

    # load additional settings that will override the defaults in settings.py. eg
    # $ export SLAPDASH_SETTINGS=/some/path/prod_settings.py
    server.config.from_envvar('SLAPDASH_SETTINGS', silent=True)

    return server


def create_dash(server):
    app = Dash(__name__, server=server)

    app.title = server.config['TITLE']
    app.config.routes_pathname_prefix = server.config['ROUTES_PATHNAME_PREFIX']

    # Suppress callback validation as we will be initialising callbacks that target
    # element IDs that won't yet occur in the layout.
    app.config.supress_callback_exceptions = True

    return app


# The Flask instance
server = create_app()

# The Dash instance
app = create_dash(server)

# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # load the rest of our Dash app
    from . import aqa_index

    # configure the Dash instance's layout
    app.layout = main_aqa_layout()
    # app.layout = main_layout_sidebar


