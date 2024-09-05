import dash_bootstrap_components as dbc
from dash import html

def get_card_component(title, data1, data2):
    component = dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H5(title),
                            html.Center("avg =" + data1 +" "+ data2),
                            # html.Center("")
                        ]),
                        color="dark",
                        outline=True,
                        className = 'text-dark',
                        style={'textAlign': 'center', 'margin-bottom': '20px'}
                    ),
                )
    return component

def get_card_component2(title, data1, data2):
    component = dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H5(title),
                            html.Center("r = " + data1),
                            html.Center("p = " +data2)
                        ]),
                        color="dark",
                        outline=True,
                        className = 'text-dark',
                        style={'textAlign': 'center', 'margin-bottom': '20px'}
                    ),
                )
    return component