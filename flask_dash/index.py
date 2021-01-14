import base64
import json
import logging
import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import flask
import pandas as pd
from dash.dependencies import Input, Output
from flask import send_from_directory

from flask_dash.app import app
from flask_dash.pages import dynamic, fixed, home

logging.basicConfig(filename="local.log", level=logging.DEBUG)
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.environ.get("CONFIG_FILE", f"{dir_path}/local_config.json"), "r") as f:
    config = json.load(f)


server = flask.Flask(__name__)
external_stylesheets = []
external_stylesheets.append(dbc.themes.BOOTSTRAP)
external_stylesheets.append(dbc.themes.DARKLY)
dash_settings = config["dash_settings"]
dash_settings["server"] = server
dash_settings["external_stylesheets"] = external_stylesheets

app = dash.Dash(__name__, **dash_settings)
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config.update(config)

# toolbar = DebugToolbarExtension(app)
local_df = pd.read_csv(
    "https://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"
)


remote_df = pd.read_csv(
    "https://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"
)
colors = {"background": "#AAA", "text": "#7FDBFF"}


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/home")),
        dbc.NavItem(dbc.NavLink("Fixed", href="/fixed")),
        dbc.NavItem(dbc.NavLink("Dynamic", href="/dynamic")),
    ],
    brand=app.title,
    brand_href="/",
    sticky="top",
)

url_bar_navbar_content = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(children=[navbar, html.Div(id="page-content")]),
    ]
)


def serve_layout():
    if flask.has_request_context():
        return url_bar_navbar_content
    return html.Div(
        [
            url_bar_navbar_content,
            home.layout(),
        ]
    )


app.layout = serve_layout


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):

    if pathname in ["/", "/home", "/index"]:
        return home.layout()
    elif pathname == "/fixed":
        return fixed.layout()

    elif pathname == "/dynamic":
        return dynamic.layout()

    else:
        return "Error 404"


if __name__ == "__main__":
    app.logger.info("Processing default request")
    debug = app.config.get("DEBUG", False)
    app.run_server(debug=debug, threaded=True)
    # app.run_server(host='0.0.0.0', debug=True, threaded=True)
