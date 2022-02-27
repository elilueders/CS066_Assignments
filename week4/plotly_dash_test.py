import plotly.express as px
import requests

response = requests.get("https://api.covid19api.com/live/country/united-states")

data = response.json()

fig = px.line(data, x="Date", y="Deaths", color="Province", title='COVID Deaths in the US')
fig.show()