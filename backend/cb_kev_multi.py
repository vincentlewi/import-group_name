from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json

cb_kev_multi_bp = Blueprint('cb_kev_multi', __name__)

cors = CORS(cb_kev_multi_bp)

df_movies_full = pd.read_csv("datasets/to_use/movies_web_app_with_id_final.csv", dtype = {'movieId': int}) #still have UI information 
df_movies = df_movies_full.iloc[:, 7:]
df_movies_original = df_movies.copy() #still have movieId
df_movies.set_index('movieId', inplace=True)

# dummy_list = [
#             {
#                 'title': 'The Shawshank Redemption (1994)', 
#                 'user_rating': 4.5
#             },
#             {
#                 'title': 'Pulp Fiction (1994)', 
#                 'user_rating': 4.5
#             },
#             {
#                 'title': 'The Silence of the Lambs (1991)', 
#                 'user_rating': 4
#             },
#             {
#                 'title': 'Forrest Gump (1994)', 
#                 'user_rating': 3.5
#             },
#             {
#                 'title': 'The Avengers (2012)', 
#                 'user_rating': 2.5
#             },
#             {
#                 'title': 'Avatar (2009)', 
#                 'user_rating': 2
#             },
#             {
#                 'title': 'Guardians of the Galaxy (2014)', 
#                 'user_rating': 4.5
#             },
#             {
#                 'title': 'American History X (1998)', 
#                 'user_rating': 4
#             },
#             {
#                 'title': 'Reservoir Dogs (1992)', 
#                 'user_rating': 4
#             },
#             {
#                 'title': 'No Country for Old Men (2007)', 
#                 'user_rating': 5,
#                 'movieId': '55820'
#             }
#         ]

# user_cart_json = json.dumps(dummy_list, indent=4)
# user_cart = json.loads(user_cart_json) #in the future will take json from user directly

# print(user_cart)

#get the highest rated movie
# highest_rated = max(user_cart, key=lambda x: x['user_rating'])
# movie_id = int(highest_rated['movieId'])
# movie_name = highest_rated['title']
# print(movie_id)
# print(movie_name)

@cb_kev_multi_bp.route('/cb_kev_multi', methods=['GET', 'POST'])
def post_cb_kev_multi():
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
            if i>=50:
                break
        # print('loop done')
        # print(final_dict)
        final_dict_json = json.dumps(final_dict, indent=4)
        # print(final_dict_json)
        return final_dict       
     
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