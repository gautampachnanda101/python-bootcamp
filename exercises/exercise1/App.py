from datetime import datetime


def hello_world():
    print("Hello World!")

def draw_triangle():
    print("   /|")
    print("  / |")
    print(" /  |")
    print("/___|")
def print_gap():
    print("=====================================")
def print_new_line():
    print()
def variables_concat():
    character_name = "Peter"
    year = 1980
    current_year=datetime.now().year
    friend_name = "James"
    friend_age_diff = 10
    peters_age = str(current_year - year)
    james_age = str(current_year - year - friend_age_diff)
    print_gap()
    print(f"There once was character called " + character_name + " who was "+ peters_age + " years old.")
    print("He had a friend called " + friend_name+ " who was " + james_age + " years old.")
    print_new_line()
def print_sentence(character_name ="Peter", year = 1980, friend_name ="James", friend_age_diff = 10):
    current_year=datetime.now().year
    character_age=current_year-year
    friend_age=current_year-year-friend_age_diff
    print_gap()
    title=get_title(True,character_age)
    friend_title=get_title(False,friend_age)
    print(f"There once was character called {title} {character_name} who was {character_age} years old.")
    print(f"He had a friend called {friend_title} {friend_name} who was {friend_age} years old.")
    print_new_line()
def get_title(is_male = False, age: int = 0):
    if is_male:
        if age>18:
            return "Mr."
        else:
            return "Master"
    else:
        if age>18:
            return "Ms."
        else:
            return "Miss."
hello_world()
draw_triangle()
print_new_line()
variables_concat()
print_sentence()
print_sentence("Jimmy", 1980, "Helena", 35)