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


server = flask.Flask(__name__)
external_stylesheets = []
external_stylesheets.append(dbc.themes.BOOTSTRAP)
external_stylesheets.append(dbc.themes.DARKLY)


external_scripts = [
    {
        "src": "https://use.fontawesome.com/releases/v5.0.13/js/solid.js",
        "integrity": "sha384-tzzSw1/Vo+0N5UhStP3bvwWPq+uvzCMfrN1fEFe+xBmv1C/AtVX5K0uZtmcHitFZ",
        "crossorigin": "anonymous",
    },
    {
        "src": "https://use.fontawesome.com/releases/v5.0.13/js/fontawesome.js",
        "integrity": "sha384-6OIrr52G08NpOFSZdxxz1xdNSndlD4vdcf/q2myIUVO0VsqaGHJsB0RaBE01VTOY",
        "crossorigin": "anonymous",
    },
    {
        "src": "https://code.jquery.com/jquery-3.3.1.slim.min.js",
        "integrity": "sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo",
        "crossorigin": "anonymous",
    },
    {
        "src": "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js",
        "integrity": "sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ",
        "crossorigin": "anonymous",
    },
    {
        "src": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js",
        "integrity": "sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm",
        "crossorigin": "anonymous",
    },
]

dash_settings = config["dash_settings"]
dash_settings["server"] = server

dash_settings["external_stylesheets"] = external_stylesheets
dash_settings["external_scripts"] = external_scripts
app = dash.Dash(__name__, **dash_settings)

# TODO: set a 'SECRET_KEY' to enable the Flask session cookies
app.config.update(config)

colors = {"background": "#AAA", "text": "#7FDBFF"}

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Dash", className="display-4"),
        html.Hr(),
        html.P("Assignment 4", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink(
                    "Home", href="/page-1", id="page-1-link", external_link=True
                ),
                dbc.NavLink(
                    "Static", href="/page-2", id="page-2-link", external_link=True
                ),
                dbc.NavLink(
                    "Dynamic", href="/page-3", id="page-3-link", external_link=True
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Page 1 is the root
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):

    if pathname in ["/", "/home", "/index", "/page-1"]:
        return home.layout()
    elif pathname in ["/fixed", "/page-2"]:
        return fixed.layout()

    elif pathname in ["/dynamic", "/page-3"]:
        return dynamic.layout()

    else:
        dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )


# todo: Add caching for storing daily data, currently disabled through the configuration
# Redis cache will suffice to memoize
# the caching can be enabled by using the @cache.cached() decorator
# cache_enabled = app.config.get("cache", {}).get("enabled", False)
# if cache_enabled:
#
#     CACHE_CONFIG = {
#         "CACHE_TYPE": "redis",
#         "CACHE_REDIS_URL": app.config.get("cache", {}).get("url"),
#     }
#     cache.init_app(app, config=CACHE_CONFIG)
# else:
#     # CACHE_CONFIG = {
#     #     "DEBUG": True,  # some Flask specific configs
#     #     "CACHE_TYPE": "simple",  # Flask-Caching related configs
#     #     "CACHE_DEFAULT_TIMEOUT": 3000
#     # }
#     CACHE_CONFIG = {"CACHE_TYPE": "simple"}


if __name__ == "__main__":
    app.logger.info("Processing default request")
    debug = app.config.get("DEBUG", False)
    app.run_server(debug=debug)
