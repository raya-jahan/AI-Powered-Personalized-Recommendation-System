import pandas as pd
from scipy.sparse import csr_matrix

# Load data
data = pd.read_csv('ml-latest-small/ml-latest-small/ratings.csv')

# Create a user-item interaction matrix
user_item_matrix = data.pivot(index='userId', columns='movieId', values='rating').fillna(0)
# Compressed Sparse Row matrix
interaction_matrix = csr_matrix(user_item_matrix)

print("User-Item Matrix Shape:", user_item_matrix.shape)
