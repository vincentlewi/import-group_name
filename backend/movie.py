from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import pandas as pd
import numpy as np
# import tensorflow as tf

# df = pd.read_csv('datasets/movielens_original/ratings.csv')
# df_movie = pd.read_csv('datasets/movielens_original/movies.csv')

movie_bp = Blueprint('movie', __name__)

cors = CORS(movie_bp)

df_movie = pd.read_csv('datasets/to_use/movies_web_app_with_id_final.csv')

@movie_bp.route('/', methods=['GET', 'POST'])
def get_all():
    # GET request
    if request.method == 'GET':
        return df_movie.sort_values(by='num_of_rating', ascending=False).head(1000).sample(100).to_json(orient='records')
    
    if request.method == 'POST':
        data = request.get_json()
        movie_ids = [item['movieId'] for item in data.values()]
        return df_movie[df_movie['movieId'].isin(movie_ids)].to_json(orient='records')
    
@movie_bp.route('/search/<string:search>', methods=['GET'])
def search(search):
    # GET request
    if request.method == 'GET':
        df_search = df_movie[df_movie.title.apply(lambda x: search in x.lower())].head(20).rename(columns={'movieId': 'value', 'title': 'label'})
        return df_search[['value', 'label']].to_json(orient='records')

# new_model = tf.keras.models.load_model('sa1ved_model/my_model')