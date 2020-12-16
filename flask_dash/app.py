import os
import json

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
import dash
import dash_core_components as dcc
import dash_html_components as html

import logging

logging.basicConfig(filename="local.log", level=logging.DEBUG)
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.environ.get("CONFIG_FILE", f"{dir_path}/local_config.json"), "r") as f:
    config = json.load(f)

server = Flask(__name__)

app = dash.Dash(name="Flask Dash App", server=server)
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config.update(config)
# app.debug = True
# toolbar = DebugToolbarExtension(app)

colors = {"background": "#AAA", "text": "#7FDBFF"}

app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.H1(
            children="This is a H1 ",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="Dash: Sample Flask App",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        dcc.Graph(
            id="example-graph-2",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "line", "name": "Fridge"},
                    {"x": [1, 2, 3], "y": [2, 4, 5], "type": "line", "name": "Freezer"},
                ],
                "layout": {
                    "images": [
                        {
                            "xref": "paper",
                            "yref": "paper",
                            "x": 1,
                            "y": 1.05,
                            "sizex": 0.2,
                            "sizey": 0.2,
                            "xanchor": "right",
                            "yanchor": "bottom",
                        }
                    ],
                    "plot_bgcolor": colors["background"],
                    "paper_bgcolor": colors["background"],
                    "font": {"color": colors["text"]},
                },
            },
        ),
    ],
)

if __name__ == "__main__":
    app.logger.info("Processing default request")
    debug = app.config.get("DEBUG", False)
    app.run_server(debug=debug)
