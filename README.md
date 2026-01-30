# Movies Report Generator
This Python application parses a CSV file containing movies data and generates multiple reports.
The user can specify reports by year, genre, or top movies by votes.

Reports include:

1) Highest and lowest rating movies in a given year, with average runtime
2) Number of movies and average rating for a specific genre
3) Top movies by number of votes

## Features

1. Generate reports for a given year (`-r`)
2. Generate reports for a specific genre (`-g`)
3. Generate top-voted movies for a given year (`-v`)
4. Uses environment variables for CSV file path (`FILE_PATH`) 
## Steps to Follow
- `git clone https://github.com/Binteimran853/Python-Assignment-1.git`
- `cd Python-Assignment-1`

### Set the CSV file path
Create a .env file in the root directory:
FILE_PATH='/full/path/to/movies.csv'
example=> FILE_PATH = '/Users/dev/downloads/movies.csv'

### Package
`pip install python-dotenv`

## How TO Run:
- `python movies_parser.py -r 1903`       # Year report
- `python movies_parser.py -g Comedy`      # Genre report
- `python movies_parser.py -v 1895`        # Top votes report
- `python movies_parser.py -r 1903 -g Comedy -v 1895`   # Multiple reports

#### Note: Use 'python3' in CLI instead of 'python' if system have python3
