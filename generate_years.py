import json

# Load parsed_movies.json
with open("parsed_movies.json", "r") as f:
    movies = json.load(f)

# Extract MovieID and Year to create parsed_years.json
parsed_years = {"MovieID": movies["MovieID"], "Year": movies["Year"]}

# Save to JSON
with open("parsed_years.json", "w") as f:
    json.dump(parsed_years, f, indent=4)

print("Generated parsed_years.json")
