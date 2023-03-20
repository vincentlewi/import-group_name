from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json

combo_bp = Blueprint('combo', __name__)

cors = CORS(combo_bp)

dummy_cf = {
  "0": {
    "movieId": 44,
    "title": "Mortal Kombat (1995)",
    "score": 1.0000000000000002
  },
  "1": {
    "movieId": 2617,
    "title": "The Mummy (1999)",
    "score": 1.0000000000000002
  },
  "2": {
    "movieId": 4270,
    "title": "The Mummy Returns (2001)",
    "score": 1.0000000000000002
  },
  "3": {
    "movieId": 4367,
    "title": "Lara Croft: Tomb Raider (2001)",
    "score": 1.0000000000000002
  },
  "4": {
    "movieId": 5313,
    "title": "The Scorpion King (2002)",
    "score": 1.0000000000000002
  },
  "5": {
    "movieId": 5463,
    "title": "Reign of Fire (2002)",
    "score": 1.0000000000000002
  },
  "6": {
    "movieId": 6564,
    "title": "Lara Croft Tomb Raider: The Cradle of Life (2003)",
    "score": 1.0000000000000002
  },
  "7": {
    "movieId": 7373,
    "title": "Hellboy (2004)",
    "score": 1.0000000000000002
  },
  "8": {
    "movieId": 7454,
    "title": "Van Helsing (2004)",
    "score": 1.0000000000000002
  },
  "9": {
    "movieId": 45722,
    "title": "Pirates of the Caribbean: Dead Man's Chest (2006)",
    "score": 1.0000000000000002
  },
  "10": {
    "movieId": 57640,
    "title": "Hellboy II: The Golden Army (2008)",
    "score": 1.0000000000000002
  }
}


dummy_cb_kev = {
  "0": {
    "movieId": 431,
    "title": "Carlito's Way (1993)",
    "score": 1.0000000000000002
  },
  "1": {
    "movieId": 593,
    "title": "The Silence of the Lambs (1991)",
    "score": 1.0000000000000002
  },
  "2": {
    "movieId": 1245,
    "title": "Miller's Crossing (1990)",
    "score": 1.0000000000000002
  },
  "3": {
    "movieId": 2194,
    "title": "The Untouchables (1987)",
    "score": 1.0000000000000002
  },
  "4": {
    "movieId": 4034,
    "title": "Traffic (2000)",
    "score": 1.0000000000000002
  },
  "5": {
    "movieId": 5464,
    "title": "Road to Perdition (2002)",
    "score": 1.0000000000000002
  },
  "6": {
    "movieId": 44665,
    "title": "Lucky Number Slevin (2006)",
    "score": 1.0000000000000002
  },
  "7": {
    "movieId": 48516,
    "title": "The Departed (2006)",
    "score": 1.0000000000000002
  },
  "8": {
    "movieId": 115569,
    "title": "Nightcrawler (2014)",
    "score": 1.0000000000000002
  },
  "9": {
    "movieId": 219722,
    "title": "Crash (I) (2004)",
    "score": 1.0000000000000002
  },
  "10": {
    "movieId": 233738,
    "title": "Joker (I) (2019)",
    "score": 1.0000000000000002
  }
}

@combo_bp.route('/combo', methods=['GET', 'POST'])
def get_combo():
    # GET request
    if request.method == 'POST':
        user_cart = json.loads(request.data) #in the future will take json from user directly
        # print(user_cart)
        highest_rated = max(user_cart, key=lambda x: x['user_rating'])
        movie_id = int(highest_rated['movieId'])
        movie_name = highest_rated['title']
        # print(movie_id)
        # print(movie_name)
        # test

        target_movie = df_movies.loc[[movie_id]]
        normalised_df_movies = df_movies.astype(np.float32)
        cosine_sim = cosine_similarity(normalised_df_movies, target_movie)

        similar_movies = list(enumerate(cosine_sim.flatten()))
        # print(similar_movies)
        sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)

        # print(sorted_similar_movies)

        def get_info_from_index(index):
            movieId = int(df_movies_original.iloc[index]['movieId'])
            title = df_movies_full[df_movies_full.movieId == movieId]["title"].values[0]
            return movieId, title
        
        target_movie_cosine_sim_index = df_movies_original.index[df_movies_original['movieId'] == movie_id].values[0] #get 0-based index in cosine similarity array of the target movie
        i=0
        final_dict = {}

        for movie in sorted_similar_movies:
            if movie[0] == target_movie_cosine_sim_index:
                continue
            # print(get_title_from_index(movie[0]))
            movieId, title = get_info_from_index(movie[0])
            score = movie[1]
            final_dict[i] = {
                'movieId': movieId,
                'title': title,
                'score': score
            }
            i=i+1
            if i>=50:
                break
        final_dict_json = json.dumps(final_dict, indent=4)
        print(final_dict_json)
        return final_dict  