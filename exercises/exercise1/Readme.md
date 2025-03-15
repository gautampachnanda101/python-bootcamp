# Exercise 1: Hello World!
This exercise is designed to help you get started with Python programming. You will create a simple Python script that prints "Hello World!" to the console and then create a few more functions to practice basic Python syntax.

### `hello_world()`
Learn how to create a Python script. Use the `print()` function to print a string to the console.

Steps:
- Create a file App.py  
- Write a function that prints "Hello World!" to the console.
- Run the script using the Python interpreter and verify that it prints the expected output.

### `draw_triangle()`
Learn how to define a function in Python. Create a function that prints a simple ASCII art representation of a triangle to the console.

Steps:
- Add a function to the file that prints a simple ASCII art representation of a triangle to the console.
- Call the function to verify that it prints the expected output.
- The console output should look like this:
```
   /\
  /  \
 /    \
/______\
```


### `print_gap()`
Add a function to the file that prints a line of equal signs (`=`) to the console to create a visual gap.
Prints a line of equal signs (`=`) to the console to create a visual gap.

Steps:
- Add a function to the file that prints a line of equal signs (`=`) to the console.
- Call the function to verify that it prints the expected output.
- The console output should look like this:

```python
====================
```
### `print_new_line()`
Create a function that prints a new line to the console.
Prints a new line to the console.

Steps:
- Add a function to the file that prints a new line to the console.
- Call the function to verify that it prints the expected output.
- The console output should contain a blank line.


### `variables_concat()`
Create a function that initializes two variables, `first_name` and `last_name`, with your first and last name, respectively. Then, print the concatenation of the two variables to the console.
- Initializes several variables: `character_name`, `year`, `current_year`, `friend_name`, `friend_age_diff`.
- Calculates `peters_age` and `james_age` based on the current year and the given years.
- Prints a formatted story about Peter and his friend James using the calculated ages.

Steps:
- Add a function to the file that initializes two variables, `first_name` and `last_name`, with your first and last name, respectively.
- Print the concatenation of the two variables to the console.
- Call the function to verify that it prints the expected output.
- The console output should look like this:
```python
Hello, World!
```


### `print_sentence(character_name="Peter", year=1980, friend_name="James", friend_age_diff=10)`
- Takes four parameters: `character_name`, `year`, `friend_name`, and `friend_age_diff`.
- Calculates the current year, `character_age`, and `friend_age`.
- Prints a formatted story about the character and their friend using the calculated ages and titles obtained from the `get_title` function.

### `get_title(is_male=False, age: int=0)`
Create a function that returns a title based on the
- Takes two parameters: `is_male` and `age`.
- Returns a title based on the gender and age of the character:
  - "Mr." for males over 18.
  - "Master" for males 18 or younger.
  - "Ms." for females over 18.
  - "Miss." for females 18 or younger.