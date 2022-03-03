# x = int(input("Enter a wikipedia page title (-1 to quit):"))

    
# while not x == -1:
#     print(x)
#     x = int(input("continue? "))
    
#     if x == 1:
#         print("heyo!")
    
import requests

endpoint = "https://en.wikipedia.org/w/rest.php/v1/page/"
response = requests.get(endpoint+"Iron oxide").json()
for k in response:
    print(k, type(response[k]))
print(response["key"])