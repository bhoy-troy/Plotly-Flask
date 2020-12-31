import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

style = {"textDecoration": "underline", "color": "#1F77B4"}


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


def layout():
    return html.Div(
        [
            html.H1("Home"),
            html.Div(
                [
                    dcc.Link(
                        "Dynamic Data",
                        href="/page-2",
                        style=style,
                    )
                ]
            ),
            html.Div(
                [
                    dcc.Link(
                        "Static Data",
                        href="/page-1",
                        style={"textDecoration": "underline", "color": "#1F77B4"},
                    )
                ]
            ),
        ],
        style=style,
    )
