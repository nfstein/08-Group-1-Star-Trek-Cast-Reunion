import json

with open('guest_movies.txt', 'r') as file:
    guest_movies = json.load(file)
    guest_movies = {int(id_str): guest_movies[id_str] for id_str in guest_movies}
    
with open('guest_stars.txt', 'r') as file:
    guest_stars = json.load(file)
    guest_stars = {int(id_str): guest_stars[id_str] for id_str in guest_stars}
    
with open('main_cast_movies.txt', 'r') as file:
    main_cast_movies = json.load(file)
    main_cast_movies = {int(id_str): main_cast_movies[id_str] for id_str in main_cast_movies}
    
with open('main_cast_stars.txt', 'r') as file:
    main_cast_stars = json.load(file)
    main_cast_stars = {int(id_str): main_cast_stars[id_str] for id_str in main_cast_stars}
        
with open('star_trek_tos.txt', 'r') as file:
    star_trek_tos = json.load(file)
