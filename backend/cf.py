import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import model_selection
from sklearn.model_selection import train_test_split
import math

ratings = pd.read_csv('dataset/to_use')