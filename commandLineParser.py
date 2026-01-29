import argparse

def command_line_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--year-report', type=int)
    parser.add_argument('-g', '--genres', type=str)
    parser.add_argument('-v', '--vote-report', type=int)
    args = parser.parse_args()
    if  not any(vars(args).values()):
        parser.error('At least one report flag must be provided ')
    return args