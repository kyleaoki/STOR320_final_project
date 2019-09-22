import pandas as pd
import json

Movies = pd.read_csv('/Users/admin/Desktop/STOR 320 Final Project/tmdb_5000_movies.csv')


# Replacing JSON format genres column with simpler list genres

genres = Movies['genres']
genres = genres.apply(json.loads)

for index, genre in enumerate(genres):
    lst1 = []
    for name in genre:
        lst1.append(name['name'])
    Movies.at[index, 'genres'] = lst1


# Replacing JSON format keywords column with a list

keywords = Movies['keywords']
keywords = keywords.apply(json.loads)

for index, keyword in enumerate(keywords):
    lst1 = []
    for name in keyword:
        lst1.append(name['name'])
    Movies.at[index, 'keywords'] = lst1


# Replacing JSON format production companies with strings

production_companies = Movies['production_companies']
production_companies = production_companies.apply(json.loads)

for index, production_company in enumerate(production_companies):
    lst1 = []
    for name in production_company:
        lst1.append(name['name'])
    Movies.at[index, 'production_companies'] = lst1


# Replace JSON format production countries with strings

production_countries = Movies['production_countries']
production_countries = production_countries.apply(json.loads)

for index, production_country in enumerate(production_countries):
    lst1 = []
    for name in production_country:
        lst1.append(name['name'])
    Movies.at[index, 'production_countries'] = lst1


# Replace JSON format spoken languages with strings

spoken_languages = Movies['spoken_languages']
spoken_languages = spoken_languages.apply(json.loads)

for index, spoken_language in enumerate(spoken_languages):
    lst1 = []
    for name in spoken_language:
        lst1.append(name['name'])
    Movies.at[index, 'spoken_languages'] = lst1


# Command to write new CSV file, commented out:

# Movies.to_csv('/Users/admin/Desktop/cleaned_movies_dataset.csv')
