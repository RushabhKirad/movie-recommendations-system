import streamlit as st
from utils.recommender import load_movie_data, build_similarity_matrix, get_recommendations

# ❗ Must be the first Streamlit command
st.set_page_config(page_title="Movie Recommender", layout="centered")

# Load data and similarity matrix once
@st.cache_data
def setup():
    movies_df = load_movie_data()
    sim_matrix = build_similarity_matrix(movies_df)
    return movies_df, sim_matrix

movies_df, sim_matrix = setup()

# --------------- Streamlit UI ------------------

st.title("🎬 Movie Recommender System")
st.markdown("Get movie recommendations based on your favorite movie's genres.")

# Movie selection
movie_list = movies_df['title'].sort_values().tolist()
selected_movie = st.selectbox("Choose a movie:", movie_list)

# Recommend button
if st.button("Recommend"):
    with st.spinner("Finding similar movies..."):
        recommendations = get_recommendations(selected_movie, movies_df, sim_matrix)

    if recommendations[0] == "Movie not found in dataset.":
        st.error("Movie not found in dataset.")
    else:
        st.success("Top Recommendations:")
        for idx, title in enumerate(recommendations, start=1):
            st.write(f"**{idx}. {title}**")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Rushabh Kirad")
# This is the main Streamlit app for the movie recommender system.
# It allows users to select a movie and get recommendations based on genre similarity.