SPACER="-------------------------------------------------"
NEWLINE="\n"
def print_app_name( appName = "Functions"):
    print(f"App Name: {appName}")
def print_spacer():
    print(long_spacer())
def long_spacer():
    return  f"{SPACER}{SPACER}{SPACER}"
def is_adult(age: int):
    if age >= 18:
        return True
    else:
        return False
def get_title(is_male=False, age: int=0):
    if is_male:
        if is_adult(age):
            return "Mr."
        else:
            return "Master"
    else:
        if is_adult(age):
            return "Ms."
        else:
            return "Miss."
