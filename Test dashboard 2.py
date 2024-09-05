import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from dash import Dash, html, dcc, callback, Output, Input

# read data
df = pd.read_csv("test data.csv")

# Calc means
avg_fer_cap = df["Ferritin capillary"].mean()
avg_fer_men = df["Ferritin menstrual"].mean()
avg_hb_cap = df["Hb capillary"].mean()
avg_hb_men = df["Hb menstrual"].mean()

# Calc standard deviation
std_fer_cap = round(df["Ferritin capillary"].std(), 4)
std_fer_men = round(df["Ferritin menstrual"].std(), 4)
std_hb_cap = round(df["Hb capillary"].std(), 4)
std_hb_men = round(df["Hb menstrual"].std(), 4)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Card componenet thing?
def get_card_component(title, data1, data2):
    component = dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H5(title),
                            html.Center(data1),
                            html.Center(data2)
                        ]),
                        color="dark",
                        outline=True,
                        className = 'text-dark',
                        style={'textAlign': 'center', 'margin-bottom': '20px'}
                    ),
                )
    return component

# Have a go at laying the app out
app.layout = html.Div([
    html.H1(children="EVE dashboard", style={"textAlign": "center", "padding-bottom": "20px"}),
    dbc.Row([
        # get_card_component("Total participants", format(len(df.index))),
        get_card_component("Ferritin in capillary blood", str(avg_fer_cap), str(std_fer_cap)),
        get_card_component("Ferritin in menstrual blood", str(avg_fer_men), str(std_fer_men)),
        get_card_component("Hemoglobin  in capillary blood", str(avg_hb_cap), str(std_hb_cap)),
        get_card_component("Hemoglobin in menstrual blood", str(avg_hb_men), str(std_hb_men))
    ]),
    dbc.Row(
        dbc.Col([
            html.H4("Correlation Comparisons"),
            html.Div(
                dbc.RadioItems(
                    id="correlation-radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-dark",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "Ferritin, capillary blood", "value": "Ferritin capillary"},
                        {"label": "Ferritin, menstrual blood", "value": "Ferritin menstrual"},
                        {"label": "Hemoglobin, capillary blood", "value": "Hb capillary"},
                        {"label": "Hemoglobin, menstrual blood", "value": "Hb menstrual"}
                    ],
                    value="Ferritin capillary",
                ),
                className="radio-group",
                style={"margin-top": "20px"}
            ),
            dcc.Graph(figure={}, id="correlation-graph")
        ])
    ),
], style={"margin": "50px 50px 50px 50px"})

@callback(
    Output("correlation-graph", "figure"),
    Input("correlation-radios", "value")
)

def update_graph(value):
    figure = px.scatter(df, y=value)

    return figure

if __name__ == "__main__":
    app.run(debug=True)

