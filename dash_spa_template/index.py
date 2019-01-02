from flask import current_app as server
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from .app import app
from .pages import page_not_found, page1, page2, page3
from .utils import get_url


#
# The router
#

# Ordered iterable of routes: tuples of (route, menu_option and layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
urls = (
    ('',      'Page 1', page1.get_layout),
    ('page1', 'Page 1', page1.get_layout),
    ('page2', 'Page 2', page2.get_layout),
    ('page3', 'Page 3', page3.get_layout),
)


routes = {get_url(route): layout for route, _, layout in urls}
menu_options = {get_url(route): menu_option for route, menu_option, _ in urls if route != ''}


# def navbar(active_route=None):
#     _navbar = dbc.Navbar(
#         # id=server.config['NAVBAR_CONTAINER_ID'],
#         children=[
#             dbc.NavLink(navbar_option, href=route, active=route == active_route)
#             for route, navbar_option, _ in urls if route != ''
#         ],
#         brand="Example",
#         sticky="top",
#     )
#     return _navbar


def navbar(active_route=None):
    children = [
        dbc.NavLink(navbar_option, href=route, active=route == active_route)
        for route, navbar_option, _ in urls if route != ''
    ]
    return children


@app.callback(Output(server.config['CONTENT_CONTAINER_ID'], 'children'),
              [Input('url', 'pathname')])
def router(pathname):
    """The router"""
    default_layout = lambda: page_not_found(pathname)
    return routes.get(pathname, default_layout)()


#
# The Navbar
#

if server.config['NAVBAR']:
    @app.callback(Output('navbar', 'children'),
                  [Input('url', 'pathname')])
    def update_nav(pathname):
        """Create the navbar with the current page set to active"""
        if pathname is None:
            # pathname is None on the first load of the app; ignore this
            raise PreventUpdate("Ignoring first url.pathname callback")
        # return Navbar(items=server.config['NAV_ITEMS'], current_path=pathname)
        return navbar(pathname)
