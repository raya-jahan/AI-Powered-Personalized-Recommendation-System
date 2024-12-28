import pandas as pd

# Load dataset
ratings = pd.read_csv('ml-latest-small/ml-latest-small/ratings.csv')
# ratings = pd.read_csv(r'C:\Users\priyo\Downloads\rec\ml-latest-small\ratings.csv')
movies = pd.read_csv('ml-latest-small/ml-latest-small/movies.csv')

# Merge ratings and movies data
data = pd.merge(ratings, movies, on='movieId')

# Display sample data
print(data.head())
