import csv

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = []
        for row in reader:
          movie_info.append(row)
        return movie_info

movie_data = fetch_movie_data(movie_csv) 
print(movie_data)
