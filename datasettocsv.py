import json
import csv

def json_to_csv(json_file, csv_file, keys):
    with open(json_file, "r") as jf:
        data = json.load(jf)
    with open(csv_file, "w", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=keys)
        writer.writeheader()
        for i in range(len(data[keys[0]])):
            row = {key: data[key][i] for key in keys}
            writer.writerow(row)

# Convert relations
json_to_csv("relations_R1.json", "relations_R1.csv", ["MovieID", "Year", "Title"])
json_to_csv("relations_R2.json", "relations_R2.csv", ["MovieID", "Genre"])
json_to_csv("relations_R3.json", "relations_R3.csv", ["MovieID", "Director"])
