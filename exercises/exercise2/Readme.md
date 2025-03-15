# Exercise 1: Hello World!
This exercise is designed to help you get started with Python programming. You will create a simple Python script that prints "Hello World!" to the console and then create a few more functions to practice basic Python syntax.

### "Create function that can be imported and used in other scripts, using the `import` statement & newline character"
Improve knowledge of creating reusable functions and importing them into your script.

Steps:
- Create a file Functions.py  
- Create function that allow you to print a title of the exercise to the console.
- Add another function that prints a line of equal signs (`-`) to the console to create a visual gap and new line.
- Create the function in App.py that imports the functions from Functions.py and calls them to print the title and a visual gap to the console and prints the following sentence using what you have leaned so far.
expected output:

```console
App Name: Exercise 2 - functions
------------------------------------------------------------------------------------------------------------

There once was character called Mr. Phil Foden who was 45 years old.
He had a friend called Miss. Peter Caine who was 10 years old.
```

### Use functions len(), str(), int(), float(), input(), type()
Improve knowledge of using functions `len()`, `str()`, `int()`, `range()`.
Learn loops , conditional statements and try.

Steps:
- Add the character count of the sentence to the console.
- Add an input function that asks for how many times you want to print the sentence.
- Add a conditional statement that checks if the input is a number.
- Add a loop that prints the sentence the number of times specified by the user. see example below
- The function should fail gracefully if the user enters a non-numeric value.

**Expected console output: Assuming the number of times to print the sentence is 3.**

```console
App Name: Exercise 2 - Creating Functions and using imports
---------------------------------------------------------------------------------------------------------------------------------------------------
How many times would you like to print the sentence?3

Printing sentence 1 of 3
There once was character called Mr. Phil Foden who was 45 years old. He had a friend called Miss. Peter Caine who was 10 years old.
---------------------------------------------------------------------------------------------------------------------------------------------------
The above sentence contained 131 characters.
---------------------------------------------------------------------------------------------------------------------------------------------------

Printing sentence 2 of 3
There once was character called Mr. Phil Foden who was 45 years old. He had a friend called Miss. Peter Caine who was 10 years old.
---------------------------------------------------------------------------------------------------------------------------------------------------
The above sentence contained 131 characters.
---------------------------------------------------------------------------------------------------------------------------------------------------

Printing sentence 3 of 3
There once was character called Mr. Phil Foden who was 45 years old. He had a friend called Miss. Peter Caine who was 10 years old.
---------------------------------------------------------------------------------------------------------------------------------------------------
The above sentence contained 131 characters.
---------------------------------------------------------------------------------------------------------------------------------------------------
```