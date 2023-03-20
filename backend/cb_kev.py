from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json

# import tensorflow as tf

# df = pd.read_csv('datasets/movielens_original/ratings.csv')
# df_movie = pd.read_csv('datasets/movielens_original/movies.csv')

cb_kev_bp = Blueprint('kev_cb', __name__)

cors = CORS(cb_kev_bp)

df_movies_full = pd.read_csv("datasets/to_use/movies_web_app_with_id_final.csv", dtype = {'movieId': int}) #still have UI information 
df_movies = df_movies_full.iloc[:, 7:]
df_movies_original = df_movies.copy() #still have movieId
df_movies.set_index('movieId', inplace=True)

dummy_list = [
            {
                'title': 'The Shawshank Redemption (1994)', 
                'user_rating': 4.5
            },
            {
                'title': 'Pulp Fiction (1994)', 
                'user_rating': 4.5
            },
            {
                'title': 'The Silence of the Lambs (1991)', 
                'user_rating': 4
            },
            {
                'title': 'Forrest Gump (1994)', 
                'user_rating': 3.5
            },
            {
                'title': 'The Avengers (2012)', 
                'user_rating': 2.5
            },
            {
                'title': 'Avatar (2009)', 
                'user_rating': 2
            },
            {
                'title': 'Guardians of the Galaxy (2014)', 
                'user_rating': 4.5
            },
            {
                'title': 'American History X (1998)', 
                'user_rating': 4
            },
            {
                'title': 'Reservoir Dogs (1992)', 
                'user_rating': 4
            },
            {
                'title': 'No Country for Old Men (2007)', 
                'user_rating': 5,
                'movieId': '55820'
            }
        ]

user_cart_json = json.dumps(dummy_list, indent=4)
user_cart = json.loads(user_cart_json) #in the future will take json from user directly

# print(user_cart)

#get the highest rated movie
highest_rated = max(user_cart, key=lambda x: x['user_rating'])
movie_id = highest_rated['movieId']
movie_name = highest_rated['title']
# print(movie_id)
# print(movie_name)

@cb_kev_bp.route('/cb_kev', methods=['GET', 'POST'])
def get_cb_kev():
    # GET request
    if request.method == 'GET':

        return df_movies.head(10).to_json(orient='records')