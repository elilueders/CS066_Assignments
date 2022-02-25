from cgitb import text
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import requests
import plotly.express as px

response = requests.get(
    "https://api.covid19api.com/live/country/united-states")

DATA = response.json()

fig = px.line(DATA, x="Date", y="Deaths", color="Province",
              title='COVID Deaths in the US')

# make a list of anything included under the Province key
province_list = []
for record in DATA:
    if record["Province"] not in province_list:
        province_list.append(record["Province"])

app = Dash(__name__)

app.layout = html.Div(children=[
    dcc.Markdown(
        id="title",
        children="## COVID Dashboard"
    ),

    dcc.Dropdown(
        id="select_province_dropdown",
        options=sorted(province_list),  # makes the dropdown alphabetical
        value=["Iowa", "Nebraska", "Illinois"],
        multi=True
    ),

    dcc.Graph(
        id="province_graph",
        figure=fig
    )
])


@app.callback(
    Output("province_graph", "figure"),
    Input("select_province_dropdown", "value"),
)
def update_province_graph(selected_provinces):
    data_for_selected_provinces = []
    for record in DATA:
        if record["Province"] in selected_provinces:
            data_for_selected_provinces.append(record)
    if data_for_selected_provinces == []:  # added if statement so resolve error when nothing was selected
        # sets fig as blank fig with a little error message
        fig = px.line(title="PLEASE SELECT AT LEAST ONE PROVINCE")
    else:
        fig = px.line(data_for_selected_provinces, x="Date", y="Deaths",
                      color="Province", title="Recent Deaths in the US by Province")
    return fig


@app.callback(  # for fun -- sorts selected values alphabetically when those values are changed
    Output("select_province_dropdown", "value"),
    Input("select_province_dropdown", "value")
)
def sort_dropdown_selected(selected):
    sorted_selected = sorted(selected)
    return sorted_selected


if __name__ == '__main__':
    app.run_server(debug=True)
