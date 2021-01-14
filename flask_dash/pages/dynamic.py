import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
from flask import url_for

# from flask_dash.common.extensions import cache
# pretty cumbersome loading every request, need to memoize
# @cache.cached(timeout=50)
remote_df = pd.read_csv(
    "https://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?"
    "outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"
)


def layout():
    df = remote_df
    return html.Div(
        [
            dcc.Location(id="url", refresh=False),
            html.Div(
                children=[
                    html.H3(children="Loading Data Dynamically"),
                    # All elements from the top of the page
                    html.Div(
                        [
                            html.H3(children="Daily  Confirmed Cases"),
                            dcc.Graph(
                                id="Daily Confirmed Cases",
                                figure={
                                    "data": [
                                        {
                                            "x": df["Date"],
                                            "y": df["ConfirmedCovidCases"],
                                            "type": "bar",
                                            "name": "Confirmed Cases",
                                        }
                                    ],
                                    "layout": {"title": "Total Confirmed Cases"},
                                },
                            ),
                        ]
                    ),
                    # New Div for all elements in the new 'row' of the page
                    html.Div(
                        [
                            html.H3(children="Total Confirmed cases"),

                            dcc.Graph(
                                id="fig2",
                                figure={
                                    "data": [
                                        {
                                            "x": df["Date"],
                                            "y": df["TotalConfirmedCovidCases"],
                                            "type": "bar",
                                            "name": "Total Confirmed Cases",
                                        },

                                    ],
                                    "layout": {"title": "Total Confirmed Cases"},
                                },
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )
