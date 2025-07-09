from utils.recommender import load_movie_data, build_similarity_matrix, get_recommendations

def main():
    # Step 1: Load movie data
    movies_df = load_movie_data()

    # Step 2: Build similarity matrix
    similarity_matrix = build_similarity_matrix(movies_df)

    # Step 3: Test a recommendation
    movie_name = "Star Wars (1977)"  # You can change this
    recommendations = get_recommendations(movie_name, movies_df, similarity_matrix)

    print(f"\nTop recommendations for '{movie_name}':")
    for idx, title in enumerate(recommendations, start=1):
        print(f"{idx}. {title}")

if __name__ == "__main__":
    main()
