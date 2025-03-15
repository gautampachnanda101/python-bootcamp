from datetime import datetime

from Functions import get_title
from Functions import print_spacer
from Functions import print_app_name

from Functions import NEWLINE
from Functions import long_spacer


def print_sentence(character_name ="Peter", year = 1980, friend_name ="James", friend_age_diff = 10):
    current_year=datetime.now().year
    character_age=current_year-year
    friend_age=current_year-year-friend_age_diff
    print_spacer()
    title=get_title(True,character_age)
    friend_title=get_title(False,friend_age)
    sentence=f"There once was character called {title} {character_name} who was {character_age} years old. He had a friend called {friend_title} {friend_name} who was {friend_age} years old."
    loop_count=input("How many times would you like to print the sentence?")
    try:
        for i in range(int(loop_count)):
            print(f"{NEWLINE}Printing sentence {i+1} of {loop_count}")
            print(f"{sentence}{NEWLINE}{long_spacer()}{NEWLINE}The above sentence contained {len(sentence)} characters.{NEWLINE}{long_spacer()}")
    except ValueError:
        print("Number of times to print the sentence must be an integer")
        exit(1)




print_app_name("Exercise 2 - Creating Functions and using imports")
print_sentence("Phil Foden", 1980, "Peter Caine", 35)