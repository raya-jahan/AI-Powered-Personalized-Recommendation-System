import streamlit as st
import pandas as pd
from sklearn.decomposition import TruncatedSVD

# Load data
ratings = pd.read_csv('ml-latest-small/ml-latest-small/ratings.csv')
movies = pd.read_csv('ml-latest-small/ml-latest-small/movies.csv')
data = pd.merge(ratings, movies, on='movieId')
user_item_matrix = data.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Build SVD model
svd = TruncatedSVD(n_components=50, random_state=42)
svd_matrix = svd.fit_transform(user_item_matrix)

# Recommend function
def recommend_movies(user_id, num_recommendations=5):
    user_ratings = svd_matrix[user_id - 1]  # Adjust for index
    similarity = svd_matrix.dot(user_ratings)
    recommendations = (-similarity).argsort()[:num_recommendations]
    return [movies.iloc[i]['title'] for i in recommendations]

# Streamlit UI
st.title("AI-Powered Personalized Recommendation System")

user_id = st.number_input("Enter User ID", min_value=1, max_value=len(user_item_matrix), value=1)
if st.button("Recommend"):
    st.write("Recommended Movies:")
    recommendations = recommend_movies(user_id)
    for movie in recommendations:
        st.write(f"- {movie}")
