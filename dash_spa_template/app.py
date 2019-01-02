from flask import Flask
from dash import Dash
import dash_bootstrap_components as dbc

from . import create_app, create_dash
from .layouts import main_layout_header
from .cache import init_cache


# The Flask instance
server = create_app()                                                       # type: Flask

# The Dash instance
app = create_dash(server, external_stylesheets=[dbc.themes.BOOTSTRAP])      # type: Dash
init_cache(app)


# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # load the rest of our Dash app (do not remove this import!)
    from . import index

    # configure the Dash instance's layout
    app.layout = main_layout_header()
