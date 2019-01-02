from aqa_ui_poc import create_app, create_dash
from aqa_ui_poc.layouts import main_layout_header

# The Flask instance
server = create_app()

# The Dash instance
app = create_dash(server)


# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # load the rest of our Dash app

    # configure the Dash instance's layout
    app.layout = main_layout_header()
    # app.layout = main_layout_sidebar


