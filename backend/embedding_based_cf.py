from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import pandas as pd
import numpy as np
# import tensorflow as tf

# df = pd.read_csv('datasets/movielens_original/ratings.csv')
# df_movie = pd.read_csv('datasets/movielens_original/movies.csv')

CF_bp = Blueprint('CF', __name__)

cors = CORS(CF_bp)

df_movie = pd.read_csv('datasets\movies_web_app_final.csv')

@CF_bp.route('/', methods=['GET'])
def get_all():
    # GET request
    if request.method == 'GET':
        return df_movie.head(10).to_json(orient='records')
    
@CF_bp.route('/search/<string:search>', methods=['GET'])
def search(search):
    # GET request
    if request.method == 'GET':
        df_search = df_movie[df_movie.title.apply(lambda x: search in x.lower())].head().rename(columns={'title': 'label'})
        df_search['value'] = df_search['label']
        return df_search[['value', 'label']].to_json(orient='records')

# new_model = tf.keras.models.load_model('saved_model/my_model')