import ast
import csv

class Guest_Star:
    """(name, id_num, movies, movie_ids) repository of data for star trek guest stars"""
    def __init__(self, name, id_num, movies, movie_ids):
        self.name = name
        self.id_num = id_num
        self.movies = movies
        self.movie_ids = movie_ids
        #could have count for number of episodes appeared in

class Movie:
    """(name, id_num, stars, star_ids, count) repository of data for star trek guest stars' movies"""
    def __init__(self, name, id_num, stars, star_ids, count):
        self.name = name
        self.id_num = id_num
        self.stars = stars
        self.star_ids = star_ids
        self.count = len(star_ids)
        
id_to_name = {}
guest_names = []
guest_ids = []
with open('id_to_name.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        id_to_name[row[0]] = row[1]
        guest_names.append(row[1])
        guest_ids.append(row[0])

movies = {}
with open('Movie_Data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movies[int(row['movie_id'])] = {'movie': row['movie'], 'movie_id': int(row['movie_id']), 'guest_names': ast.literal_eval(row['guest_names']), 'guest_ids': ast.literal_eval(row['guest_ids']), 'count': int(row['count'])}

stars = {}
with open('Guest_Star_Data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        stars[int(row['id_num'])] = {'name': row['name'], 'id_num': int(row['id_num']), 'movies': ast.literal_eval(row['movies']), 'movie_ids': ast.literal_eval(row['movie_ids'])}

movie_id_lookup_dict = {}
for id_num in movies:
    movie_id_lookup_dict[id_num] = Movie(movies[id_num]['movie'], id_num, movies[id_num]['guest_names'], movies[id_num]['guest_ids'], movies[id_num]['count'])
star_id_lookup_dict = {}
for id_num in stars:
    star_id_lookup_dict[id_num] = Guest_Star(stars[id_num]['name'], id_num, stars[id_num]['movies'], stars[id_num]['movie_ids'])

def star_id_lookup(id_num):
    return(star_id_lookup_dict[id_num])
def movie_id_lookup(id_num):
    return(movie_id_lookup_dict[id_num])    
