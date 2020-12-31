import base64
import json
import logging
import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import flask
import pandas as pd
from dash.dependencies import Input, Output
from flask import Flask, send_from_directory
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension

from flask_dash.pages import dynamic, fixed, home

logging.basicConfig(filename="local.log", level=logging.DEBUG)
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.environ.get("CONFIG_FILE", f"{dir_path}/local_config.json"), "r") as f:
    config = json.load(f)

# server = Flask(__name__)
# 
# app = dash.Dash(name="Flask Dash App", server=server)


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
# app.debug = True
# toolbar = DebugToolbarExtension(app)

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



# app.layout = html.Div(
#     style={"backgroundColor": colors["background"]},
#     children=[
#         html.H1(
#             children="This is a H1 ",
#             style={"textAlign": "center", "color": colors["text"]},
#         ),
#         html.Div(
#             children="Dash: Sample Flask App",
#             style={"textAlign": "center", "color": colors["text"]},
#         ),
#         dcc.Graph(
#             id="example-graph-2",
#             figure={
#                 "data": [
#                     {"x": [1, 2, 3], "y": [4, 1, 2], "type": "line", "name": "Fridge"},
#                     {"x": [1, 2, 3], "y": [2, 4, 5], "type": "line", "name": "Freezer"},
#                 ],
#                 "layout": {
#                     "images": [
#                         {
#                             "xref": "paper",
#                             "yref": "paper",
#                             "x": 1,
#                             "y": 1.05,
#                             "sizex": 0.2,
#                             "sizey": 0.2,
#                             "xanchor": "right",
#                             "yanchor": "bottom",
#                         }
#                     ],
#                     "plot_bgcolor": colors["background"],
#                     "paper_bgcolor": colors["background"],
#                     "font": {"color": colors["text"]},
#                 },
#             },
#         ),
#     ],
# )

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



cache_enabled = app.config.get("cache", {}).get("enabled", False)
if cache_enabled:
    # todo: Add caching for storing daily data
    CACHE_CONFIG = {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": app.config.get("cache", {}).get("url"),
    }
    cache = Cache()
    cache.init_app(server, config=CACHE_CONFIG)

if __name__ == "__main__":
    app.logger.info("Processing default request")
    debug = app.config.get("DEBUG", False)
    app.run_server(debug=debug)
