from dotenv import load_dotenv
import os
load_dotenv()

from movie import  MovieParser, ReportGenerator
from commandLineParser import command_line_parser

def main():
    args = command_line_parser()
    parser = MovieParser(os.getenv('FILE_PATH'))
    movies = parser.parse_movies()
    report = ReportGenerator()

    if args.year_report:
        report_result= report.report_year(movies, args.year_report)
        print(f'Highest rating: {report_result.highest.rating} - {report_result.highest.original_title}')
        print(f'lowest rating: {report_result.lowest.rating} - {report_result.lowest.original_title}')
        print(f'Average minutes: {report_result.avg_runtime_minutes:.2f}')

    if args.genres:
        report_result = report.report_genre(movies, args.genres)
        print(f'Movies Found: {report_result.total_movies_found}')
        print(f'Average Rating: {report_result.avg_rating:.2f}')

    if args.vote_report:
        report.report_num_votes(movies, args.vote_report)


if __name__ == '__main__':
        main()


