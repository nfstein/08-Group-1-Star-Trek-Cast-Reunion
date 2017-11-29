import json

with open('guest_movies.txt', 'r') as file:
     guest_movies = json.load(file)
with open('guest_stars.txt', 'r') as file:
     guest_stars = json.load(file)
with open('main_cast_movies.txt', 'r') as file:
     main_cast_movies = json.load(file)
with open('main_cast_stars.txt', 'r') as file:
     main_cast_stars = json.load(file)
with open('star_trek_tos.txt', 'r') as file:
     star_trek_tos = json.load(file)