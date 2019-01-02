from collections import Counter

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from ..app import app
from ..cache import register_layout, get_layout_values, update_layout_values


# ----------------------------------------------------------------------------
# Layout
# ----------------------------------------------------------------------------

# Define and register our layout cache requirements
_layout_key = 'layout-page1'
_layout_values = {
    'text-input': 'Type some text into me!',
    'sort-type': 'frequency',
    'normalize': 'no',
}
register_layout(_layout_key, _layout_values)


def get_layout():
    layout_values = get_layout_values(_layout_key)
    layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2("Character Counter"),
                            html.P(
                                """\
                                This demo counts the number of characters in the text box and updates a bar
                                chart with their frequency as yoyu type. Give it a try!"""
                            ),
                        ]
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Textarea(
                                id='text-input',
                                value=layout_values.get('text-input'),
                                style={'width': '40em', 'height': '5em'},
                            ),
                        ]
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div('Sort by:'),
                            dbc.RadioItems(
                                id='sort-type',
                                options=[
                                    {'label': 'Frequency', 'value': 'frequency'},
                                    {'label': 'Character code', 'value': 'code'},
                                ],
                                value=layout_values.get('sort-type')
                            ),
                        ]
                    ),
                    dbc.Col(
                        [
                            html.Div('Normalize character case?'),
                            dbc.RadioItems(
                                id='normalize',
                                options=[
                                    {'label': 'No', 'value': 'no'},
                                    {'label': 'Yes', 'value': 'yes'},
                                ],
                                value=layout_values.get('normalize')
                            ),
                        ]
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(id='graph'),
                        ]),

                ]
            ),
        ],
        className="mt-3",
    )

    return dbc.Container(layout)   # , className="mt-4")
    # return dbc.Container(html.Div('Test'), className="mt-4")


# ----------------------------------------------------------------------------
# Callbacks
# ----------------------------------------------------------------------------


@app.callback(
    Output('graph', 'figure'),      # Output
    [Input('text-input', 'value'),  # Inputs
     Input('sort-type', 'value'),
     Input('normalize', 'value')],  
    [],                             # States
)
def callback(text, sort_type, normalize):
    """ Update graph on input change. """

    # update layout cache with inputs changed
    update_layout_values(_layout_key, {
        'text-input': text,
        'sort-type': sort_type,
        'normalize': normalize
    })

    # process the inputs
    if normalize == 'yes':
        text = text.lower()

    if sort_type == 'frequency':
        sort_func = lambda x: -x[1]
    else:
        sort_func = lambda x: ord(x[0])
        
    counts = Counter(text)

    if len(counts) == 0:
        x_data, y_data = [], []
    else:
        x_data, y_data = zip(*sorted(counts.items(), key=sort_func))

    return {
        'data': [
            {'x': x_data, 'y': y_data, 'type': 'bar', 'name': 'trace1'},
        ],
        'layout': {
            'title': 'Frequency of Characters',
            # 'height': '600',
            'font': {'size': 12}
        },
    }
