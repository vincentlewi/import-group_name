from flask import Flask
import pandas as pd
import numpy as np

df = pd.read_csv('datasets/movielens_original/ratings.csv')
df_movie = pd.read_csv('datasets/movielens_original/movies.csv')

import tensorflow as tf
from tensorflow.keras.models import load_model

new_model = load_model('saved_model/my_model')