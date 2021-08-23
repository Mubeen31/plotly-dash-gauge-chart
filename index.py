import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.layout = html.Div([
    html.Div([
        html.H6('DHT11 Sensor Data',
                style = {
                    'line-height': '1',
                    'color': 'white'},
                className = 'adjust_title twelve columns'
                ),
    ], className = "row flex-display"),

    html.Div([
        dcc.Interval(id = 'update_chart',
                     interval = 1000,
                     n_intervals = 0),
    ]),

    html.Div([
        html.Div([
            html.Div([
                html.Div(id = 'text1', className = 'move_text_down'),
                dcc.Graph(id = 'humidity_indicator',
                          animate = False,
                          config = {'displayModeBar': 'hover'},
                          className = 'grid_height'),
            ], className = 'grid_one_column'),
            html.Div([
                html.Div(id = 'text2', className = 'move_text_down'),
                dcc.Graph(id = 'temperature_indicator',
                          animate = False,
                          config = {'displayModeBar': 'hover'},
                          className = 'grid_height'),
            ], className = 'grid_one_column'),
        ], className = 'grid_two_column'),

    ], className = "row flex-display"),

], id= "mainContainer",
   style={"display": "flex", "flex-direction": "column"})

@app.callback(Output('text1', 'children'),
              [Input('update_chart', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature']
    df = pd.read_csv('humidity_and_temperature.csv', names = header_list)
    get_time = df['Time'].tail(1).iloc[0]
    get_humi = df['Humidity'].tail(1).iloc[0].astype(float)
    previous_humi = df['Humidity'].tail(2).iloc[0].astype(float)
    change_humidity = get_humi - previous_humi
    if n_intervals == 0:
        raise PreventUpdate

    if change_humidity > 0:

     return [
        html.H6('Humidity',
                style = {
                         'color': 'white',
                         'margin-bottom': '-7px'},
                className = 'heading_title'
                ),
        html.P(get_time,
               style = {'textAlign': 'center',
                        'color': 'white',
                        'fontSize': 18,
                        'margin-top': '-3px'
                        }
               ),
        html.P('{0:,.2f}%'.format(get_humi),
               style = {'textAlign': 'center',
                        'color': '#00FF00',
                        'fontSize': 18,
                        'font-weight': 'bold',
                        'margin-top': '-3px',
                        }, className = 'paragraph_value_humi'
               ),
        html.P('+{0:,.2f}%'.format(change_humidity) + ' ' + 'vs previous period',
               style = {'textAlign': 'center',
                        'color': '#00FF00',
                        'fontSize': 12,
                        'font-weight': 'bold',
                        'margin-top': '-15px',
                        }, className = 'change_paragraph_value_humi'
               ),
    ]

    elif change_humidity < 0:

     return [
        html.H6('Humidity',
                style = {
                         'color': 'white',
                         'margin-bottom': '-7px'},
                className = 'heading_title'
                ),
        html.P(get_time,
               style = {'textAlign': 'center',
                        'color': 'white',
                        'fontSize': 18,
                        'margin-top': '-3px'
                        }
               ),
        html.P('{0:,.2f}%'.format(get_humi),
               style = {'textAlign': 'center',
                        'color': '#DE3163',
                        'fontSize': 18,
                        'font-weight': 'bold',
                        'margin-top': '-3px',
                        }, className = 'paragraph_value_humi'
               ),
        html.P('{0:,.2f}%'.format(change_humidity) + ' ' + 'vs previous period',
               style = {'textAlign': 'center',
                        'color': '#DE3163',
                        'fontSize': 12,
                        'font-weight': 'bold',
                        'margin-top': '-15px',
                        }, className = 'change_paragraph_value_humi'
               ),
    ]

    elif change_humidity == 0:

     return [
        html.H6('Humidity',
                style = {
                         'color': 'white',
                         'margin-bottom': '-7px'},
                className = 'heading_title'
                ),
        html.P(get_time,
               style = {'textAlign': 'center',
                        'color': 'white',
                        'fontSize': 18,
                        'margin-top': '-3px'
                        }
               ),
        html.P('{0:,.2f}%'.format(get_humi),
               style = {'textAlign': 'center',
                        'color': 'white',
                        'fontSize': 18,
                        'font-weight': 'bold',
                        'margin-top': '-3px',
                        }, className = 'paragraph_value_humi'
               ),
        html.P('{0:,.2f}%'.format(change_humidity) + ' ' + 'vs previous period',
               style = {'textAlign': 'center',
                        'color': 'white',
                        'fontSize': 12,
                        'font-weight': 'bold',
                        'margin-top': '-15px',
                        }, className = 'change_paragraph_value_humi'
               ),
    ]

@app.callback(Output('text2', 'children'),
              [Input('update_chart', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature']
    df = pd.read_csv('humidity_and_temperature.csv', names = header_list)
    get_time = df['Time'].tail(1).iloc[0]
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    previous_temp = df['Temperature'].tail(2).iloc[0].astype(float)
    change_temperature = get_temp - previous_temp
    if n_intervals == 0:
        raise PreventUpdate

    if change_temperature > 0:

        return [
        html.H6('Temperature',
                style = {
                    'color': 'white',
                    'margin-bottom': '-7px'},
                className = 'heading_title'
                ),
        html.P(get_time,
               style = {'textAlign': 'center',
                        'color': 'white',
                        'fontSize': 18,
                        'margin-top': '-3px'
                        }
               ),
        html.P('{0:,.2f}°C'.format(get_temp),
               style = {'textAlign': 'center',
                        'color': '#00FF00',
                        'fontSize': 18,
                        'font-weight': 'bold',
                        'margin-top': '-3px',
                        }, className = 'paragraph_value_temp'
               ),
        html.P('+{0:,.2f}°C'.format(change_temperature) + ' ' + 'vs previous period',
               style = {'textAlign': 'center',
                        'color': '#00FF00',
                        'fontSize': 12,
                        'font-weight': 'bold',
                        'margin-top': '-15px',
                        }, className = 'change_paragraph_value_temp'
               ),
    ]

    elif change_temperature < 0:
        return [
            html.H6('Temperature',
                    style = {
                        'color': 'white',
                        'margin-bottom': '-7px'},
                    className = 'heading_title'
                    ),
            html.P(get_time,
                   style = {'textAlign': 'center',
                            'color': 'white',
                            'fontSize': 18,
                            'margin-top': '-3px'
                            }
                   ),
            html.P('{0:,.2f}°C'.format(get_temp),
                   style = {'textAlign': 'center',
                            'color': '#DE3163',
                            'fontSize': 18,
                            'font-weight': 'bold',
                            'margin-top': '-3px',
                            }, className = 'paragraph_value_temp'
                   ),
            html.P('{0:,.2f}°C'.format(change_temperature) + ' ' + 'vs previous period',
                   style = {'textAlign': 'center',
                            'color': '#DE3163',
                            'fontSize': 12,
                            'font-weight': 'bold',
                            'margin-top': '-15px',
                            }, className = 'change_paragraph_value_temp'
                   ),
        ]

    elif change_temperature == 0:
        return [
            html.H6('Temperature',
                    style = {
                        'color': 'white',
                        'margin-bottom': '-7px'},
                    className = 'heading_title'
                    ),
            html.P(get_time,
                   style = {'textAlign': 'center',
                            'color': 'white',
                            'fontSize': 18,
                            'margin-top': '-3px'
                            }
                   ),
            html.P('{0:,.2f}°C'.format(get_temp),
                   style = {'textAlign': 'center',
                            'color': 'white',
                            'fontSize': 18,
                            'font-weight': 'bold',
                            'margin-top': '-3px',
                            }, className = 'paragraph_value_temp'
                   ),
            html.P('{0:,.2f}°C'.format(change_temperature) + ' ' + 'vs previous period',
                   style = {'textAlign': 'center',
                            'color': 'white',
                            'fontSize': 12,
                            'font-weight': 'bold',
                            'margin-top': '-15px',
                            }, className = 'change_paragraph_value_temp'
                   ),
        ]

@app.callback(
    Output('humidity_indicator', 'figure'),
    [Input('update_chart', 'n_intervals')])
def update_confirmed(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature']
    df = pd.read_csv('humidity_and_temperature.csv', names = header_list)
    get_humi = df['Humidity'].tail(1).iloc[0].astype(float)
    if n_intervals == 0:
        raise PreventUpdate

    return {
        'data': [go.Indicator(
            mode = 'gauge',
            value = get_humi,
            gauge = {'axis': {'range': [None, 100], 'tickcolor': "white"},
                     'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                     'bordercolor': "rgb(0, 255, 255)",
                     'borderwidth': 0.5,
                     'threshold': {'line': {'color': "white", 'width': 2},
                                   'thickness': 1, 'value': 70}
                     },
            # number = {'valueformat': '.2f',
            #           'font': {'size': 20},
            #
            #           },
            domain = {'y': [0, 1], 'x': [0, 1]})],
        'layout': go.Layout(
            title = {'text': '',
                     'y': 0.8,
                     'x': 0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'
                     },
            font = dict(color = 'white'),
            paper_bgcolor = 'rgba(255, 255, 255, 0)',
            plot_bgcolor = 'rgba(255, 255, 255, 0)',
        ),

    }

@app.callback(
    Output('temperature_indicator', 'figure'),
    [Input('update_chart', 'n_intervals')])
def update_confirmed(n_intervals):
    header_list = ['Time', 'Humidity', 'Temperature']
    df = pd.read_csv('humidity_and_temperature.csv', names = header_list)
    get_time = df['Time'].tail(20)
    get_humi = df['Temperature'].tail(1).iloc[0].astype(float)
    if n_intervals == 0:
        raise PreventUpdate

    return {
        'data': [go.Indicator(
            mode = 'gauge',
            value = get_humi,
            gauge = {'axis': {'range': [None, 40], 'tickcolor': "white"},
                     'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                     'bordercolor': "rgb(0, 255, 255)",
                     'borderwidth': 0.5,
                     'threshold': {'line': {'color': "white", 'width': 2},
                                   'thickness': 1, 'value': 25}
                     },
            # number = {'valueformat': '.2f',
            #           'font': {'size': 20},
            #
            #           },
            domain = {'y': [0, 1], 'x': [0, 1]})],
        'layout': go.Layout(
            title = {'text': '',
                     'y': 0.8,
                     'x': 0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'
                     },
            font = dict(color = 'white'),
            paper_bgcolor = 'rgba(255, 255, 255, 0)',
            plot_bgcolor = 'rgba(255, 255, 255, 0)',
        ),

    }

if __name__ == "__main__":
    app.run_server(debug=True)
