import json

with open("HighestGrossingMovies.json") as moviefile:
    movies = json.load(moviefile)


def most_popular_in_genre(movieList, genre):
    result = ""  # I wanted to make this more elegant but this is the best I could make sense it so far
    best_world_sales = 0
    for m in movies:
        if (genre in (m["Genre"])) and (m["World Sales"] > best_world_sales):
            result = m
            best_world_sales = result["World Sales"]
    return result


print(most_popular_in_genre(movies, "Comedy"))
