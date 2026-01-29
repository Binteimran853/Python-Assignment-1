import os, csv
import heapq
class Movie:
    def __init__(self, id, title_type, original_title, start_year, runtime_minutes, genres, rating, num_votes):
        self.id = id
        self.title_type = title_type
        self.original_title = original_title
        self.start_year = start_year
        self.runtime_minutes = runtime_minutes
        self.genres = genres
        self.rating = rating
        self.num_votes = num_votes

    def display(self):
        print(self.id)
        print(self.title_type)
        print(self.original_title)
        print(self.start_year)
        print(self.runtime_minutes)
        print(self.genres)
        print(self.rating)
        print(self.num_votes)


class MovieParser:
    def __init__(self, FILE_PATH):
        self.FILE_PATH = FILE_PATH
        self.movies = []

    def parse(self):
        with open(os.getenv('FILE_PATH'), 'r') as file_object:
            reader_obj = csv.DictReader(file_object)
            for row in reader_obj:
                self.movies.append(
                    Movie(id = row['id'],
                          title_type = row['titleType'],
                          original_title = row['originalTitle'],
                          genres = list(row['genres'].split(',')),
                          start_year = int(row['startYear']),
                          runtime_minutes = int(row['runtimeMinutes']) if row['runtimeMinutes'] not in (None, '', '\\N') else 0,
                          rating = float(row['rating']),
                          num_votes = int(row['numVotes'])
                          )
                )
        return self.movies


class ReportGenerator:

    def __init__(self):
        self.year_movies = []

    def report_by_year(self, movies, year):
        for obj in movies:
            if obj.start_year == year:
                self.year_movies.append(
                    Movie(id = obj.id,
                          title_type = obj.title_type,
                          original_title = obj.original_title,
                          genres = obj.genres,
                          start_year = obj.start_year,
                          runtime_minutes = obj.runtime_minutes,
                          rating = obj.rating,
                          num_votes = obj.num_votes

                    ))
        highest = max(self.year_movies, key = lambda obj: obj.rating)
        lowest = min(self.year_movies, key = lambda obj: obj.rating)
        avg_runtime_minutes = sum(obj.runtime_minutes for obj in self.year_movies) / len(self.year_movies)
        return highest, lowest, avg_runtime_minutes

    def report_by_genre(self,movies, genre):
        objects = [obj for obj in movies if genre in obj.genres]
        rating = [obj.rating for obj in objects]
        return len(objects), sum(rating) / len(objects)

    def report_by_num_votes(self, movies, year):
        self.year_movies = [obj for obj in movies if obj.start_year == year]
        top_ten_movies = heapq.nlargest(10, self.year_movies , key = lambda obj: obj.num_votes)
        result = top_ten_movies[0].num_votes // 80
        print(top_ten_movies[0].original_title, '😀 '* 80, top_ten_movies[0].num_votes)
        for top_movie in top_ten_movies[1:]:
            print(top_movie.original_title,'😀 ' *(top_movie.num_votes // result), top_movie.num_votes)
        return top_ten_movies



