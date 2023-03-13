from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
# import tensorflow as tf
# from tensorflow.keras.models import load_model

# df = pd.read_csv('datasets/movielens_original/ratings.csv')
# df_movie = pd.read_csv('datasets/movielens_original/movies.csv')

app = Flask(__name__)   

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/recommend', methods=['GET', 'POST'])
def index():
    # GET request
    if request.method == 'GET':
        return 'GET'

    # POST request
    if request.method == 'POST':
        return 'POST'

if __name__ == '__main__':
    app.run(port=5000, debug=True)

# new_model = load_model('saved_model/my_model')