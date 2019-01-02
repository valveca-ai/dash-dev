import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output
import dash_bootstrap_components as dbc

from ..app import app
from ..cache import register_layout, get_layout_values, update_layout_values


# ----------------------------------------------------------------------------
# Layout
# ----------------------------------------------------------------------------

# Define and register our layout cache requirements
_layout_key = 'layout-page2'
_layout_values = {}
register_layout(_layout_key, _layout_values)


tab1 = dbc.Card(
    [
        dbc.CardTitle("Page 2, tab 1 contents"),
        dbc.CardText("You can replace this with whatever you like"),
    ],
    body=True,
)

tab2 = dbc.Card(
    [
        dbc.CardTitle("Page 2, tab 2 contents"),
        dbc.CardText("Let's write something different here for fun"),
    ],
    body=True,
)

page2 = dbc.Tabs(
    [
        dbc.Tab(tab1, label="Tab 1", className="mt-3"),
        dbc.Tab(tab2, label="Tab 2", className="mt-3"),
    ]
)

layout = page2


def get_layout():
    return layout


# ----------------------------------------------------------------------------
# Callbacks
# ----------------------------------------------------------------------------
