from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
# import tensorflow as tf


CF_CB_bp = Blueprint('CF_CB', __name__)

cors = CORS(CF_CB_bp)

# GETTING VINCENT'S EMBEDDED MOVIES

ratings = pd.read_csv('datasets/movielens_original/ratings.csv')
movies = pd.read_csv('datasets/movielens_original/movies.csv')
ratings = ratings[['movieId', 'rating']]
movies = movies[['movieId', 'title']]

M = ratings['movieId'].nunique()
movie_inv_mapper = dict(zip(list(range(M)), np.unique(ratings["movieId"])))

from tensorflow.keras.models import load_model
model = load_model('backend/CF_CB.h5')

dict_weights = {}
for layer in model.layers:
    if layer.name in ["users_embeddings", "movies_embeddings"]:
        dict_weights[layer.name] = layer.weights
weights = pd.DataFrame(dict_weights["movies_embeddings"][0].numpy())
df_movies_embeddings = pd.DataFrame(dict_weights["movies_embeddings"][0].numpy())
df_movies_embeddings.columns = ["emb_ " + str(col) for col in df_movies_embeddings.columns]
df_movies_embeddings.reset_index(inplace=True)
df_movies_embeddings.rename(columns={"index":"movieId"}, inplace=True)
df_movies_embeddings = df_movies_embeddings.merge(movies[["movieId", "title"]].drop_duplicates(), how="left", on="movieId").dropna()

# df_movies_embeddings['movieId'] = df_movies_embeddings['movieId'].apply(lambda x: movie_inv_mapper[x])
# print(df_movies_embeddings)
#APPLYING SAME NAME CONVENTIONS AS cb_kev_multi
df_movies_full = df_movies_embeddings #still have title and moveId
# print(df_movies_full)
df_movies_original = df_movies_embeddings.drop('title', axis=1) #still have title
# print(df_movies_original)
df_movies = df_movies_original.set_index('movieId')
# print(df_movies)

@CF_CB_bp.route('/CF_CB', methods=['GET', 'POST'])
def post_CF_CB():
    if request.method == 'POST':
        user_cart = json.loads(request.data)
        # print(user_cart)

        rating_df = pd.DataFrame(user_cart)
        rating_df = rating_df[['movieId', 'userRating']]
        user_movies = df_movies_original[df_movies_original['movieId'].isin(rating_df['movieId'].tolist())]
        
        rating_df.set_index('movieId', inplace=True)
        # print(rating_df)
        user_movies.set_index('movieId', inplace=True)
        # print(user_movies)
        # print(rating_df)
        # print(user_movies)
        userProfile = rating_df.transpose().dot(user_movies)
        userProfile = userProfile / user_movies.shape[0]
        # print('this is the user profile')
        # print(userProfile)

        normalised_df_movies = df_movies.astype(np.float32)
        cosine_sim = cosine_similarity(normalised_df_movies, userProfile)
        similar_movies = list(enumerate(cosine_sim.flatten()))
        sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)
        # print(sorted_similar_movies[:51])

        def get_info_from_index(index):
            movieId = int(df_movies_original.iloc[index]['movieId'])
            title = df_movies_full[df_movies_full.movieId == movieId]["title"].values[0]
            return movieId, title
        
        i=0
        final_dict = {}
        for movie in sorted_similar_movies:
            # print('this is movie' + str(i))
            movieId, title = get_info_from_index(movie[0])
            # title = get_title_from_index(movie[0])
            # print(title)
            score = movie[1]
            # print(score)
            final_dict[i] = {
                'movieId': movieId,
                'title': title,
                'score': score
            }
            i=i+1
            if i>=100:
                break
        # print('loop done')
        # print(final_dict)
        final_dict_json = json.dumps(final_dict, indent=4)
        # print(type(final_dict_json))
        return final_dict_json

        # rating_df = pd.DataFrame(user_cart)
        # rating_df = rating_df[['movieId', 'userRating']]
        # # print('works until here')
        # final_dict = {
        #     0: {
        #     'title': 'No Country for Old Men (2007)', 
        #     'score': 5,
        #     'movieId': '55820'
        #     }
        # }
        # final_dict_json = json.dumps(final_dict, indent=4)
        # # print(final_dict_json)
        # return final_dict_json       