# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from dotenv import load_dotenv
import os
load_dotenv()
from movie import  MovieParser, ReportGenerator
from commandLineParser import command_line_parser




def main():
    args = command_line_parser()
    parser = MovieParser(os.getenv('FILE_PATH'))
    movies = parser.parse()
    report = ReportGenerator()
    if args.year_report:
        report.report_by_year(movies, args.year_report)
        highest, lowest, avg_mean_minutes = report.report_by_year(movies, args.year_report)
        print(f'Highest rating: {highest.rating} - {highest.original_title}')
        print(f'lowest rating: {lowest.rating} - {lowest.original_title}')
        print(f'Average minutes: {avg_mean_minutes:.2f}')

    if args.genres:
        movies_found, avg_mean_rating = report.report_by_genre(movies, args.genres)
        print(f'Movies Found: {movies_found}')
        print(f'Average Rating: {avg_mean_rating:.1f}')
    if args.vote_report:
        top_ten_movies = report.report_by_num_votes(movies, args.vote_report)
        print(f'Movies Found: {top_ten_movies}')



if __name__ == '__main__':
        main()


