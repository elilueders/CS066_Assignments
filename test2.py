import plotly.express as px
import requests


response = requests.get("https://api.covid19api.com/summary")

data = response.json()
country_data = data["Countries"]

fig = px.bar(country_data,x="Country",y="NewConfirmed",title="New Confirmed Cases by Country")
fig.show()
