import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



style = {"text-decoration": "underline", "color": "#1F77B4"}


def layout():
    return html.Div(
        [
            html.H1("Home"),
            html.Div(
                [
                    dcc.Link(
                        "Dynamic Data",
                        href="/dynamic",
                        style=style,
                    )
                ]
            ),
            html.Div(
                [
                    dcc.Link(
                        "Static Data",
                        href="/fixed",
                        style={"text-decoration": "underline", "color": "#1F77B4"},
                    )
                ]
            ),
        ],
        style=style,
    )
