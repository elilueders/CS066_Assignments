import json

with open("HighestGrossingMovies.json") as moviefile:
    movies = json.load(moviefile)
    
print(movies[0])