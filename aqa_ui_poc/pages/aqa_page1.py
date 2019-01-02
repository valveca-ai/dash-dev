import dash_bootstrap_components as dbc
import dash_html_components as html

from ..aqa_app import app


# define content for page 1
page1 = dbc.Card(
    [
        dbc.CardTitle("Page 1 contents"),
        dbc.CardText("You can replace this with whatever you like"),
    ],
    body=True,
)

layout = html.Div(page1)
