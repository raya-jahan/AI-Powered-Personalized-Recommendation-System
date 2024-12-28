from sklearn.decomposition import TruncatedSVD
from user_item_matrix import user_item_matrix
from load_and_preprocess import movies

# Apply SVD; Collaborative filtering: Similar users with same interests in movies
# are recommended/suggested same movie
# We use 0 and 1 to classify; And also we use Normalizing 
svd = TruncatedSVD(n_components=50, random_state=42)
svd_matrix = svd.fit_transform(user_item_matrix)

print("SVD Matrix Shape:", svd_matrix.shape)

# Recommend movies
def recommend_movies(user_id, num_recommendations=5):
    user_ratings = svd_matrix[user_id - 1]  # Adjust for index
    similarity = svd_matrix.dot(user_ratings)
    recommendations = (-similarity).argsort()[:num_recommendations]
    return [movies.iloc[i]['title'] for i in recommendations]

# Example: Recommend for user 1
print(recommend_movies(1))
