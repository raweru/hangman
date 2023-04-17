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
