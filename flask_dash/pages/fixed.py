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
                                children="Fixed",
                            )
                        ],
                    )
                ],
            ),
            html.Div(
                className="Row",
                # children=[
                #     html.Div(className="col-lg-2"),
                #     html.Div(
                #         className="col-lg-8",
                #         children=[
                #             html.Div(
                #                 className="col-lg-6",
                #                 children=[
                #                     html.Img(
                #                         className="img-responsive",
                #                         src="/static/plotly(8).png",
                #                     ),
                #                     html.Img(
                #                         className="img-responsive",
                #                         src="/static/plotly(9).png",
                #                     ),
                #                 ],
                #             ),
                #             html.Div(
                #                 className="col-lg-6",
                #                 children=[
                #                     html.Img(
                #                         className="img-responsive",
                #                         src="/static/plotly(10).png",
                #                     ),
                #                     html.Img(
                #                         className="img-responsive",
                #                         src="/static/plotly(12).png",
                #                     ),
                #                 ],
                #             ),
                #         ],
                #     ),
                #     html.Div(className="col-lg-2"),
                # ],
            ),
        ]
    )
