import os
# Refactoring Leidy Viviana Osorio
# Define the constants for severity threshold and the file path
SEVERITY_THRESHOLD = 50
ERROR_FILE_PATH = 'data/error.log'

def read_logs(file_path):
    """Reads the log file and returns a list of processed entries."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.rstrip().split(' ') for line in lines]

def filter_severe_errors(entries):
    """Filters and sorts errors based on severity threshold and timestamp."""
    severe_errors = [
        entry for entry in entries 
        if entry[0] == 'E' and int(entry[1]) > SEVERITY_THRESHOLD
    ]
    return sorted(severe_errors, key=lambda x: int(x[2]))

def display_errors(errors):
    """Prints the errors to the screen."""
    for error in errors:
        print(' '.join(error))

def process_logs():
    entries = read_logs(ERROR_FILE_PATH)
    severe_errors = filter_severe_errors(entries)
    display_errors(severe_errors)

def main():
    process_logs()

if __name__ == '__main__':
    main()

