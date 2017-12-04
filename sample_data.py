import json
import os

filepath = os.path.join('data', 'sample_movies.txt')
with open(filepath, 'r') as file:
    sample_movies = json.load(file)
    sample_movies = {int(id_str): sample_movies[id_str] for id_str in sample_movies}

filepath = os.path.join('data', 'sample_stars.txt')
with open(filepath, 'r') as file:
    sample_stars = json.load(file)
    sample_stars = {int(id_str): sample_stars[id_str] for id_str in sample_stars}