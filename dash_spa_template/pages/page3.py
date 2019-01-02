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


page3 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Heading"),
                        html.P(
                            """\
Donec id elit non mi porta gravida at eget metus.
Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
odio dui."""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

layout = page3


def get_layout():
    return layout


# ----------------------------------------------------------------------------
# Callbacks
# ----------------------------------------------------------------------------
