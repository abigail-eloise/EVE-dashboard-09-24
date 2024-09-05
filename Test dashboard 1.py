import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import dcc
from dash import html

# import dash_core_components as dcc
# import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ----------------------------------------------------
# Let's try using pandas to clean the data
df = pd.read_csv("test data.csv")

df.dropna(subset=["Ferritin capillary"], inplace=True)
# print(df)

# ---------------------------------------------------
# App layout......
app.layout = html.Div([

    html.H1("Python Dashboard attempt 1", style={'text-align': 'center'}),

    dcc.Checklist(id="select_type",
                  options=[
                     {"label": "Ferritin capillary", "value": "Ferritin capillary"},
                     {"label": "Ferritin menstrual", "value": "Ferritin menstrual"},
                     {"label": "Hemoglobin capillary", "value": "Hb capillary"},
                     {"label": "Hemoglobin menstrual", "value": "Hb menstrual"}]
                 ),
    html.Div(id="not_sure", children=[]),
    html.Br(),

    dcc.Graph(id="blood_comparison", figure={})
])

# -----------------------------------------------
# Okay now we try and do the weird stuff
@app.callback(
    [Output(component_id="not_sure", component_property="children"),
     Output(component_id="blood_comparison", component_property="figure")],
    [Input(component_id="select_type", component_property="value")]
)

# Okay now link to the graph I think??
def update_graph(option_selected):
    dff = df.copy()
    dff = dff[option_selected]

    container = f"Blood component(s) chosen: {option_selected}"

    fig = px.scatter(
        data_frame=dff,
        title="Blood comparison"
    )
    return container, fig


# ------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True)

