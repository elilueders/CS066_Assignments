import requests

url = "https://api.covid19api.com/live/country/united-states"
response = requests.get(url)

DATA = response.json()
i=0
for x in DATA[0]:
    i+=1
    print(i,x)