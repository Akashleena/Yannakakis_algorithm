import json  # Ensure the json module is imported

def parse_movies(file_path):
    """
    Parses the movies.list file into a dictionary of lists.

    Returns:
    - dict: A dictionary representing the movies relation.
    """
    movies = {"MovieID": [], "Title": [], "Year": []}
    try:
        movie_id = 1
        with open(file_path, "r", encoding="latin-1", errors="replace") as file:
            for line in file:
                if "--------------------" in line:
                    break  # Skip header

            for line in file:
                parts = line.rsplit("\t", 1)
                if len(parts) == 2:
                    title, year = parts
                    try:
                        # Extract the first year in case of ranges (e.g., "1994-1995")
                        year = int(year.split("-")[0].strip())
                        movies["MovieID"].append(movie_id)
                        movies["Title"].append(title.strip())
                        movies["Year"].append(year)
                        movie_id += 1
                    except ValueError:
                        # Skip invalid entries
                        print(f"Skipping invalid year format: {year.strip()} for title {title.strip()}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    return movies

if __name__ == "__main__":
    file_path = "/home/dell/yannakakis_algorithm/ftp.fu-berlin.de/pub/misc/movies/database/frozendata/movies.list"
    movies = parse_movies(file_path)

    # Save to JSON for reuse
    output_path = "/home/dell/yannakakis_algorithm/parsed_movies.json"
    with open(output_path, "w") as f:
        json.dump(movies, f, indent=4)

    # Print confirmation message and first 5 rows for verification
    print(f"Parsed movies saved to {output_path}")
    print({key: value[:5] for key, value in movies.items()})
