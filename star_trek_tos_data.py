import json
import os

filepath = os.path.join('data', 'guest_movies.txt')
with open(filepath, 'r') as file:
    guest_movies = json.load(file)
    guest_movies = {int(id_str): guest_movies[id_str] for id_str in guest_movies}

filepath = os.path.join('data', 'guest_stars.txt')   
with open(filepath, 'r') as file:
    guest_stars = json.load(file)
    guest_stars = {int(id_str): guest_stars[id_str] for id_str in guest_stars}

filepath = os.path.join('data', 'main_cast_movies.txt')   
with open(filepath, 'r') as file:
    main_cast_movies = json.load(file)
    main_cast_movies = {int(id_str): main_cast_movies[id_str] for id_str in main_cast_movies}

filepath = os.path.join('data', 'main_cast_stars.txt') 
with open(filepath, 'r') as file:
    main_cast_stars = json.load(file)
    main_cast_stars = {int(id_str): main_cast_stars[id_str] for id_str in main_cast_stars}

filepath = os.path.join('data', 'star_trek_tos.txt')        
with open(filepath, 'r') as file:
    star_trek_tos = json.load(file)
