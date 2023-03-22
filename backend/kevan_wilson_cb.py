from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
import json

kevan_wilson_cb_bp = Blueprint('kevan_wilson_cb', __name__)

cors = CORS(kevan_wilson_cb_bp)

df_movies_full = pd.read_csv("datasets/to_use/movies_web_app_with_id_final.csv", dtype = {'movieId': int}) #still have UI information 
df_movies = df_movies_full.iloc[:, 7:]
df_movies_original = df_movies.copy() #still have movieId
df_movies.set_index('movieId', inplace=True)

@kevan_wilson_cb_bp.route('/kevan_wilson_cb_bp', methods=['GET', 'POST'])
def kevan_wilson_cb_bp():
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
            if i>=10:
                break
        # print('loop done')
        # print(final_dict)
        final_dict_json = json.dumps(final_dict, indent=4)
        # print(type(final_dict_json))
        return final_dict_json
     
    # if request.method == 'GET':
    #     target_movie = df_movies.loc[[movie_id]]
    #     normalised_df_movies = df_movies.astype(np.float32)
    #     cosine_sim = cosine_similarity(normalised_df_movies, target_movie)

    #     similar_movies = list(enumerate(cosine_sim.flatten()))
    #     # print(similar_movies)
    #     sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)

    #     # print(sorted_similar_movies)

    #     def get_title_from_index(index):
    #         movieId = df_movies_original.iloc[index]['movieId']
    #         return df_movies_full[df_movies_full.movieId == movieId]["title"].values[0]
    #     target_movie_cosine_sim_index = df_movies_original.index[df_movies_original['movieId'] == movie_id].values[0] #get 0-based index in cosine similarity array of the target movie
    #     i=0
    #     final_dict = {}
    #     for movie in sorted_similar_movies:
    #         if movie[0] == target_movie_cosine_sim_index:
    #             continue
    #         # print(get_title_from_index(movie[0]))
    #         title = get_title_from_index(movie[0])
    #         score = movie[1]
    #         final_dict[i] = {
    #             'title': title,
    #             'score': score
    #         }
    #         i=i+1
    #         if i>=50:
    #             break
    #     return final_dict
    #     return df_movies.head(10).to_json(orient='records')