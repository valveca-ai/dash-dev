from flask import current_app as server
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# from .exceptions import ValidationError
# from .components import Col, Row, Header


"""Contains layouts suitable for being the value of the 'layout' attribute of
Dash app instances."""


navbar_children = [
    dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
    dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
]

navbar = dbc.Navbar(navbar_children, brand="Example", sticky="top")


def main_aqa_layout():
    """Dash layout with a top-header"""

    layout = html.Div(
        [
            # html.Div(
            #     id=server.config['NAVBAR_CONTAINER_ID'],
            #     children=[
            #         navbar
            #     ],
            #     # id="header",
            #     # children=[
            #     #     # Header(),
            #     #     html.Div(
            #     #         id=server.config['NAVBAR_CONTAINER_ID'],
            #     #         children=navbar
            #     #     ),
            #     # ]
            # ),
            dcc.Location(id="url", pathname="/"),
            navbar,
            dbc.Container(id="content", style={"padding": "20px"}),
        ]
    )

    return layout

#     return html.Div([
#         html.Div(
#             id="header",
#             children=[
#                 Header(),
#                 html.Div(id=server.config['NAVBAR_CONTAINER_ID']),
#             ]
#         ),
#         html.Div(
#             className='container-fluid',
#             children=Row(
#                 Col(id=server.config['CONTENT_CONTAINER_ID'])
#             )
#         ),
#         dcc.Location(id='url', refresh=False)
#     ])
#
#
#
#
# def main_layout_header():
#     """Dash layout with a top-header"""
#     return html.Div([
#         html.Div(
#             id="header",
#             children=[
#                 Header(),
#                 html.Div(id=server.config['NAVBAR_CONTAINER_ID']),
#             ]
#         ),
#         html.Div(
#             className='container-fluid',
#             children=Row(
#                 Col(id=server.config['CONTENT_CONTAINER_ID'])
#             )
#         ),
#         dcc.Location(id='url', refresh=False)
#     ])
#
#
# # NOTE: not quite working yet
# def main_layout_sidebar():
#     """Dash layout with a sidebar"""
#     return html.Div([
#         html.Div(
#             className='container-fluid',
#             children=Row([
#                 Col(
#                     size=2,
#                     children=[
#                         Row(Col(Header())),
#                         Row(Col(id=server.config['NAVBAR_CONTAINER_ID']))
#                     ]),
#                 Col(
#                     id=server.config['CONTENT_CONTAINER_ID'],
#                     size=10,
#                     className='offset-2'
#                 ),
#             ])
#         ),
#         dcc.Location(id='url', refresh=False)
#     ])
#
#
# def main_layout_fullpage():
#     """Top level Dash layout taking up entire window"""
#     return html.Div([
#         html.Div(
#             className='container-fluid',
#             children=Row(
#                 Col(id=server.config['CONTENT_CONTAINER_ID'])
#             )
#         ),
#         dcc.Location(id='url', refresh=False),
#     ])
