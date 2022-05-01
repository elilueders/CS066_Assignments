import json

with open("HighestGrossingMovies.json") as moviefile:
    movies = json.load(moviefile)

world_movie_sales = ChainedHashMap(size=2000)
for m in movies:
    curr_title = m["Title"]
    curr_sales = m["World Sales"]
    world_movie_sales[curr_title] = curr_sales

print(world_movie_sales)