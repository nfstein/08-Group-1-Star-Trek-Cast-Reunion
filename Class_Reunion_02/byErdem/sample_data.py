import json

with open('sample_movies.txt', 'r') as file:
    sample_movies = json.load(file)
    sample_movies = {int(id_str): sample_movies[id_str] for id_str in sample_movies}
    
with open('sample_stars.txt', 'r') as file:
    sample_stars = json.load(file)
    sample_stars = {int(id_str): sample_stars[id_str] for id_str in sample_stars}