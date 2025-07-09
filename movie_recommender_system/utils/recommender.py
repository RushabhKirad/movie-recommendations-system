import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# -------------------------
# Load and preprocess data
# -------------------------
def load_movie_data(path='data/u.item'):
    movie_columns = [
        "movie_id", "title", "release_date", "video_release_date", "IMDb_URL",
        "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime",
        "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical",
        "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
    ]

    movies = pd.read_csv(path, sep='|', names=movie_columns, encoding='latin-1')

    # Keep only useful columns
    movies = movies[['movie_id', 'title', 'Action', 'Adventure', 'Animation', "Children's",
                     'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
                     'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller',
                     'War', 'Western']]

    return movies


# -------------------------
# Build similarity matrix
# -------------------------
def build_similarity_matrix(movies_df):
    genre_matrix = movies_df.drop(['movie_id', 'title'], axis=1)
    similarity = cosine_similarity(genre_matrix)
    return similarity


# -------------------------
# Recommend movies
# -------------------------
def get_recommendations(movie_title, movies_df, similarity_matrix, top_n=5):
    # Find index of the movie
    if movie_title not in movies_df['title'].values:
        return ["Movie not found in dataset."]
    
    idx = movies_df[movies_df['title'] == movie_title].index[0]

    # Get similarity scores
    sim_scores = list(enumerate(similarity_matrix[idx]))

    # Sort by score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top N similar movies (excluding the movie itself)
    sim_scores = sim_scores[1:top_n+1]

    # Fetch movie titles
    recommended_titles = [movies_df.iloc[i[0]].title for i in sim_scores]

    return recommended_titles

