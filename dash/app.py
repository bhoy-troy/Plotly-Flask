import os

from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html


server = Flask(__name__)

app = dash.Dash(name='Bootstrap_docker_app',
                server=server)

colors = {
    'background': '#AAA',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='This is a H1 ',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: Sample Flask App', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'Fridge'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Freezer'},
            ],
            'layout': {
                'images': [
                    {
                        'xref':"paper",
                        'yref':"paper",
                        'x':1,
                        'y':1.05,
                        'sizex':0.2,
                        'sizey':0.2,
                        'xanchor':"right",
                        'yanchor':"bottom"
                }],
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    debug = os.environ.get("DASH_DEBUG", False)
    app.run_server(debug=debug)
