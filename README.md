# you can time.sleep(.3) when you're dead
## pull data without querying TMDb! no internet, no rate limits

## use star_trek_tos_data.py as a module
yields all data about each guest star cast member and movie they've been involved in. Yields 5 dictionaries: guest_movies {TMDb_id_num: TMDb_data} it's really big and might not actually be that practical; guest_stars; main_cast_movies; main_cast_stars ; star_trek_tos has all TMDb data about the show (star_trek_tos['airdate'] etc) and each episode (star_trek_tos[season_num][episode_num]: TMDb_data)

## json_data_retrieval.ipynb
populates the .txt files that star_trek_tos_data.py pulls from. It takes over an hour to run so don't run unless we really need to make changes