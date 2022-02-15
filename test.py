import requests

# response = requests.get("https://api.covid19api.com/summary")
response = requests.get("https://api.covid19api.com/summary")

data = response.json()

# for d in data:
#     if "Iowa" in (d["Province"]):
#         print(d)

# for d in data:
#     if "United States of America" in (d["Country"]):
#         print (d["NewDeaths"])

print(data)
print(len(data))
