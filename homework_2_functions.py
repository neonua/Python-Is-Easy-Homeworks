"""
This file describes work with fucntions on the example of attributes of the song
"""

# List of attributes
name = 'Beautiful Lie'  # name of the song
release_year = 2008  # release year of the song
duration_in_seconds = 309  # duration of the song in seconds


# Defining functions
def name(name = 'Beautiful Lie'):
    print(f'Name - {name}')


def release_year(release_year = 2008):
    print(f'Release year - {release_year}')


def duration_in_seconds(duration_in_seconds = 309):
    print(f'Duration in seconds - {duration_in_seconds}')

def longer_than_6_mins(duration_in_seconds = 309):
    print(f'Longer than 6 mins - {True if 360 > duration_in_seconds else False}')


# Printing part
name()
release_year()
duration_in_seconds()
longer_than_6_mins()
