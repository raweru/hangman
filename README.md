# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1 - Set up the environment

GitHub is a web-based platform for version control and collaboration that allows users to store and manage their code repositories. It offers a range of features including issue tracking, pull requests, code reviews, and project management tools.

We have set up a Github account where we will create a repository for the Hangman project.

## Milestone 2 - Create the variables for the game

### Task 1: Define the list of possible words

First task is to create a list of words containing 5 favourite fruits and assign it to a variable called word_list.

Step 1. Create a list containing the names of your 5 favorite fruits.

Step 2. Assign this list to a variable called word_list.

Step 3. Print out the newly created list to the standard output (screen).

```python
word_list = ["mango", "apple", "peach", "pear", "strawberry"]
print(word_list)
```

### Task 2: Choose a random word from the list

Next, we want to choose a random word from the list. For this we need to use the "random" module to import the **choice** method which returns a random item from a given sequence.

Step 1. Go to the first line of your file.

Step 2. Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.

Step 3: Create the random.choice method and pass the word_list variable into the choice method.

Step 4: Assign the randomly generated word to a variable called word.

Step 5: Print out word to the standard output. Run the code several times and observe the words printed out after each run.

```python
import random
word_list = ["mango", "apple", "peach", "pear", "strawberry"]
print(word_list)

word = random.choice(word_list)
print(word)
```

### Task 3: Ask the user for an input

Step 1. Using the input function, ask the user to enter a single letter.

Step 2. Assign the input to a variable called guess.

```python
import random
word_list = ["mango", "apple", "peach", "pear", "strawberry"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")
```

### Task 4: Check that the input is a single character

Usually, when taking input from users, it is best to validate that the input makes sense. 

Step 1. Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.

Step 2: In the body of the if statement, print a message that says "Good guess!".

Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

```python
import random
word_list = ["mango", "apple", "peach", "pear", "strawberry"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

## Milestone 3 - Check if the guessed character is in the word

### Task 1 : Iteratively check if the input is a valid guess

Write code that will continuously ask the user for a letter and validate it.

Create a new script called milestone_3.py. This file will contain the code for this milestone.

Step 1. Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.

In the body of the loop, write the code required for the following steps.

Step 2: Ask the user to guess a letter and assign this to a variable called guess.

Step 3. Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.

Step 4. If the guess passes the checks, break out of the loop.

Step 5: If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."

```python
import random

word_list = ["mango", "apple", "peach", "pear", "strawberry"]
word = random.choice(word_list)

while True:
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    
```

### Task 2: Check whether the guess is in the word

Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer.

Step 1. Create an if statement that checks if the guess is in the word.

Step 2. In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.

Step 3. Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.

```python
import random

word_list = ["mango", "apple", "peach", "pear", "strawberry"]
word = random.choice(word_list)

while True:
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
```

### Task 3: Create functions to run the checks

Good job so far! But your code probably doesn't look great. It's hard to tell which lines do what.

Create 2 functions, check_guess and ask_for_input functions which contain the code for those two things. The check_guess function will take the guessed letter as an argument and check if the letter is in the word.

Step 1: Define a function called check_guess. pass in the guess as a parameter for the function. Write the code for the following steps in the body of this function.

Step 2: Convert the guess into lower case.

Step 3. Move the code that you wrote to check if the guess is in the word into this function block.

The ask_for_input function.

Step 1. Define a function called ask_for_input.

Step 2. Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.

Step 3. Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.

Step 4. Outside the function, call the ask_for_input function to test your code.

```python
import random

word_list = ["mango", "apple", "peach", "pear", "strawberry"]
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha() == True:
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
```