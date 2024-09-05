import dash
from dash import html, dcc
# from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dbc_componenets import get_card_component, get_card_component2
# import statistics
from scipy.stats import pearsonr  #spearmanr
# import numpy as np
# import statsmodels as sm

# do a bit here about how to read your data - do more looking into pandas to see about updating data sets

df = pd.read_csv("../test data.csv")

# Calc means
avg_fer_cap = str(df["Ferritin capillary"].mean())
avg_fer_men = str(df["Ferritin menstrual"].mean())
avg_hb_cap = str(df["Hb capillary"].mean())
avg_hb_men = str(df["Hb menstrual"].mean())

# Calc standard deviation
std_fer_cap = "± " + str(round(df["Ferritin capillary"].std(), 4))
std_fer_men = "± " + str(round(df["Ferritin menstrual"].std(), 4))
std_hb_cap = "± " + str(round(df["Hb capillary"].std(), 4))
std_hb_men = "± " + str(round(df["Hb menstrual"].std(), 4))

# Cal the Pearson correlation
x1 = df["Ferritin capillary"]
x1 = x1.dropna()
y1 = df["Ferritin menstrual"]
y1 = y1.dropna()
fer_pear_r, fer_pear_p = pearsonr(x1, y1)
fer_pear_r = str(round(fer_pear_r, 4))
fer_pear_p = str(round(fer_pear_p, 4))

x2 = df["Hb capillary"]
x2 = x2.dropna()
y2 = df["Hb menstrual"]
y2 = y2.dropna()
hb_pear_r, hb_pear_p = pearsonr(x2, y2)
hb_pear_r = str(round(hb_pear_r, 4))
hb_pear_p = str(round(hb_pear_p, 4))

# Write an app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

# Layout of the app
app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H1("EVE dashboard", className="text-center mt-4 mb-4"),
                width=12
                )
    ),

    dbc.Row(dbc.Col(html.H3("Averages and Standard Deviation", className="text-primary"))),

    dbc.Row([

        get_card_component("Ferritin Capillary", avg_fer_cap, std_fer_cap),
        get_card_component("Ferritin Menstrual", avg_fer_men, std_fer_men),
        get_card_component("Hemoglobin Capillary", avg_hb_cap, std_hb_cap),
        get_card_component("Hemoglobin Menstrual", avg_hb_men, std_hb_men)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id="Ferritin Mean", figure=px.scatter(df, y="Ferritin menstrual")),
        ], width=4),
        dbc.Col([
            dcc.Graph(id="Ferritin Box", figure=px.box(df, y="Ferritin menstrual"))
        ], width=2),
        dbc.Col([
            dcc.Graph(id="Hb Mean", figure=px.scatter(df, y="Hb menstrual"))
        ], width=4),
        dbc.Col([
            dcc.Graph(id="Hb Box", figure=px.box(df, y="Hb menstrual"))
        ], width=2)
    ]),

    dbc.Row([dbc.Col(html.H3("Pearson Correlation Coefficient", className="text-primary"))]),

    dbc.Row([
        get_card_component2("Ferritin Correlation", fer_pear_r, fer_pear_p),
        get_card_component2("Hemoglobin Correlation", hb_pear_r, hb_pear_p)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id="Ferritin correlation",
                      figure=px.scatter(df, "Ferritin capillary", "Ferritin menstrual", trendline='ols'))
        ], width={'size': 5, 'offset': 1}
        ),
        dbc.Col([
            dcc.Graph(id="Hemoglobin correlation",
                      figure=px.scatter(df, x="Hb capillary", y="Hb menstrual", trendline='ols'))
        ], width={'size': 5}
        )
    ])
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
