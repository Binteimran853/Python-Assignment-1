import csv
import heapq
import math
from dataclasses import dataclass

@dataclass()
class Movie:
    id : str
    title_type : str
    original_title : str
    start_year : int
    runtime_minutes : int
    genres : set[str]
    rating : float
    num_votes : int

# MovieParser to parse each movie from CSV file
class MovieParser:
    def __init__(self, FILE_PATH):
        self.FILE_PATH = FILE_PATH
        self.movies = []

    def parse_movies(self):
        try:
            with open(self.FILE_PATH, 'r') as file_object:
                reader_obj = csv.DictReader(file_object)
                for row in reader_obj:
                    try:
                        self.movies.append(
                            Movie(id = row['id'],
                                  title_type = row['titleType'],
                                  original_title = row['originalTitle'],
                                  genres = set(row['genres'].lower().split(',')),
                                  start_year = int(row['startYear']),
                                  runtime_minutes = int(row['runtimeMinutes']) if row['runtimeMinutes'] not in (None, '',
                                                                                                              '\\N') else 0,
                                  rating = float(row['rating']),
                                  num_votes = int(row['numVotes'])
                                  )
                        )
                    except ValueError:
                        continue
        except FileNotFoundError:
            raise FileNotFoundError('Movie file not found')
        return self.movies


""" Data classes to store calcultaions after result """
@dataclass()
class YearReport:
    highest : Movie
    lowest : Movie
    avg_runtime_minutes : float


@dataclass()
class GenresReport:
    total_movies_found : int
    avg_rating : float


""" ReportGenerator class to peform calculations on specfic data """
class ReportGenerator:
    def __init__(self):
        self.year_movies = []

    def report_year(self, movies, year):
        self.year_movies = [movie for movie in movies if movie.start_year == year]
        if not self.year_movies:
            raise  ValueError('No recode found for this year')
        highest = max(self.year_movies, key = lambda movie: movie.rating)
        lowest = min(self.year_movies, key = lambda movie: movie.rating)
        avg_runtime_minutes = sum(movie.runtime_minutes for movie in self.year_movies) / len(self.year_movies)
        # Returns result object
        return YearReport(highest = highest,lowest = lowest,
                          avg_runtime_minutes = avg_runtime_minutes)

    def report_genre(self, movies, genre):
        movies_objects = [movie for movie in movies if genre.lower() in movie.genres]
        if not movies_objects:
            raise ValueError('No recode found for given genre')
        avg_rating = sum(movie.rating for movie in movies_objects) / len(movies_objects)
        # Returns result object
        return GenresReport(total_movies_found = len(movies_objects),
                           avg_rating = avg_rating)

    def report_num_votes(self, movies, year):
        self.year_movies = [movie for movie in movies if movie.start_year == year]
        # Raise Error if movies not found for given year
        if not self.year_movies:
            raise ValueError('No recode found for given year')
        top_ten_movies = heapq.nlargest(10, self.year_movies , key = lambda movie: movie.num_votes)
        result = math.ceil(top_ten_movies[0].num_votes / 80)
        print(top_ten_movies[0].original_title, '😀 '* 80, top_ten_movies[0].num_votes)
        for top_movie in top_ten_movies[1:]:
            print(top_movie.original_title,'😀 ' * math.ceil((top_movie.num_votes / result)), top_movie.num_votes)
        return



