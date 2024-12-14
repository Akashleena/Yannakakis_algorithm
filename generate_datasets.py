import json
import random

def generate_movies(num_movies):
    """
    Generate a synthetic R1 dataset of movies with unique MovieIDs, Titles, and Years.
    """
    movies = {"MovieID": [], "Title": [], "Year": []}
    for i in range(1, num_movies + 1):
        movies["MovieID"].append(i)
        movies["Title"].append(f"Movie_{i}")
        movies["Year"].append(random.randint(1980, 2023))  # Random years
    return movies

def generate_years(num_movies):
    """
    Generate a synthetic R2 dataset of MovieIDs and random Years.
    """
    years = {"MovieID": [], "Year": []}
    for i in range(1, num_movies + 1):
        years["MovieID"].append(i)
        years["Year"].append(random.randint(1980, 2023))
    return years

def generate_genres(num_movies):
    """
    Generate a synthetic R3 dataset of MovieIDs and random Genres.
    """
    genres = {"MovieID": [], "Genre": []}
    genre_list = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi"]
    for i in range(1, num_movies + 1):
        genres["MovieID"].append(i)
        genres["Genre"].append(random.choice(genre_list))  # Random genres
    return genres

def save_datasets(sizes):
    """
    Generate and save datasets for given sizes.
    """
    for size in sizes:
        r1 = generate_movies(size)
        r2 = generate_years(size)
        r3 = generate_genres(size)
        
        relations = {"R1": r1, "R2": r2, "R3": r3}
        filename = f"relations_{size}.json"
        with open(filename, "w") as f:
            json.dump(relations, f, indent=4)
        print(f"Saved dataset for {size} tuples as {filename}")

if __name__ == "__main__":
    sizes = [1000, 5000, 10000, 20000, 50000]
    save_datasets(sizes)
