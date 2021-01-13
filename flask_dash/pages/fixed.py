import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import url_for


def layout():
    return html.Div(
        [
            html.Div(
                className="Row",
                children=[
                    html.Div(
                        # className="col-lg-12 page-header",
                        children=[
                            html.H3(
                                className="text-center",
                                children="The number of cases by sex on a monthly basis",
                            ),
                            html.Img(
                                className="img-responsive",
                                src="/assets/images/sex.svg",
                            ),
                        ],
                    )
                ],
            ),
            html.Div(
                className="Row",
                children=[
                    html.Div(
                        children=[
                            html.H3(
                                className="text-center",
                                children="Graphing the monthly cases ",
                            ),
                            html.Img(
                                className="img-responsive",
                                src="/assets/images/monthly_cases.svg",
                            ),
                        ],
                    )
                ],
            ),
        ]
    )
