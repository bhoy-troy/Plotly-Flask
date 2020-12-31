import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
from flask import url_for

# from flask_dash.common.extensions import cache

# @cache.cached(timeout=50)
remote_df = pd.read_csv(
    "https://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"
)


def layout():
    df = remote_df

    colors = {"background": "#AAA", "text": "#7FDBFF"}

    return html.Div(
        [
            dcc.Location(id="url", refresh=False),
            html.Div(
                children=[
                    # All elements from the top of the page
                    html.Div(
                        [
                            html.H1(children="Hello Dash"),
                            html.Div(
                                children="""
            Dash: A web application framework for Python.
        """
                            ),
                            dcc.Graph(
                                id="Total Confirmed Cases",
                                figure={
                                    "data": [
                                        {
                                            "x": df["Date"],
                                            "y": df["ConfirmedCovidCases"],
                                            "type": "bar",
                                            "name": "Confirmed Cases",
                                        },
                                        # {
                                        #     "x": df["Date"],
                                        #     "y": df["ConfirmedCovidCases"],
                                        #     "type": "bar",
                                        #     "name": "Confirmed Cases",
                                        # },
                                    ],
                                    "layout": {"title": "Total Confirmed Cases"},
                                },
                            ),
                        ]
                    ),
                    # New Div for all elements in the new 'row' of the page
                    html.Div(
                        [
                            html.H1(children="Hello Dash 2"),
                            html.Div(
                                children="""
            Dash: A web application framework for Python.
        """
                            ),
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
                                        # {
                                        #     "x": df["Date"],
                                        #     "y": df["ConfirmedCovidCases"],
                                        #     "type": "bar",
                                        #     "name": "Confirmed Cases",
                                        # },
                                    ],
                                    "layout": {"title": "Total Confirmed Cases 2"},
                                },
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )


# html.Div(
# [
# html.Div(
#     className="Row",
#     children=[
#         html.Div(
#             className="col-lg-12 page-header",
#             children=[
#                 html.H3(
#                     className="text-center",
#                     children="Dynamic",
#                 )
#             ],
#         )
#     ],
# ),
# html.Div(
#     className="Row",
#     children=[
#         html.Div(className="col-lg-2"),
#         html.Div(
#             className="col-lg-8",
#             children=[
#                 html.Div(
#                     className="col-lg-6",
#                     children=[
#                         html.Img(
#                             className="img-responsive",
#                             src="/static/plotly(8).png",
#                         ),
#                         html.Img(
#                             className="img-responsive",
#                             src="/static/plotly(9).png",
#                         ),
#                     ],
#                 ),
#                 html.Div(
#                     className="col-lg-6",
#                     children=[
#                         html.Img(
#                             className="img-responsive",
#                             src="/static/plotly(10).png",
#                         ),
#                         html.Img(
#                             className="img-responsive",
#                             src="/static/plotly(12).png",
#                         ),
#                     ],
#                 ),
#             ],
#         ),
#         html.Div(className="col-lg-2"),
#     ],
# ),
#     ]
# )
