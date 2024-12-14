import json

# Load parsed_movies.json
with open("parsed_movies.json", "r") as f:
    movies = json.load(f)

# Generate genres deterministically
def generate_genres(movie_ids):
    genre_list = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi"]
    genres = {"MovieID": [], "Genre": []}
    for movie_id in movie_ids:
        genres["MovieID"].append(movie_id)
        # Assign a genre based on MovieID modulo the number of genres
        genres["Genre"].append(genre_list[movie_id % len(genre_list)])
    return genres

# Create parsed_genres.json using MovieIDs from parsed_movies.json
parsed_genres = generate_genres(movies["MovieID"])

# Save to JSON
with open("parsed_genres.json", "w") as f:
    json.dump(parsed_genres, f, indent=4)

print("Generated parsed_genres.json deterministically")



