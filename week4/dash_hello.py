from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import requests
import plotly.express as px

#read the country-level data from the API
response = requests.get("https://api.covid19api.com/summary")
DATA = response.json()
fig = px.bar(DATA["Countries"],x="Country",y="NewConfirmed",title="New Confirmed Cases by Country")

app = Dash(__name__)

app.layout = html.Div(children = [
    dcc.Markdown(
        id = "title",
        children = "## COVID Dashboard"
    ),

    dcc.Graph(
        id = "country_bar_graph",
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)