# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1 - Set up the environment

GitHub is a web-based platform for version control and collaboration that allows users to store and manage their code repositories. It offers a range of features including issue tracking, pull requests, code reviews, and project management tools.

We have set up a Github account where we will create a repository for the Hangman project.

## Milestone 2 - Create the variables for the game

### Task 1: Define the list of possible words

First task is to create a list of words containing 5 favourite fruits and assign it to a variable called word_list.

Step 1: Create a list containing the names of your 5 favorite fruits.

Step 2: Assign this list to a variable called word_list.

Step 3: Print out the newly created list to the standard output (screen).

```python
word_list = ["mango", "apple", "peach", "pear", "strawberry"]
print(word_list)
```

### Task 2: Choose a random word from the list

Next, we want to choose a random word from the list. For this we need to use the "random" module to import the **choice** method which returns a random item from a given sequence.

Step 1: Go to the first line of your file.

Step 2: Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.

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

Step 1: Using the input function, ask the user to enter a single letter.

Step 2: Assign the input to a variable called guess.

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

Step 1: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.

Step 2: In the body of the if statement, print a message that says "Good guess!".

Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

```python
import random
word_list = ["mango", "apple", "peach", "pear", "strawberry"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")
if len(guess) == 1 or guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

## Milestone 3 - Check if the guessed character is in the word

### Task 1 : Iteratively check if the input is a valid guess

Write code that will continuously ask the user for a letter and validate it.

Create a new script called milestone_3.py. This file will contain the code for this milestone.

Step 1: Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.

In the body of the loop, write the code required for the following steps.

Step 2: Ask the user to guess a letter and assign this to a variable called guess.

Step 3: Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.

Step 4: If the guess passes the checks, break out of the loop.

Step 5: If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."

```python
import random

word_list = ["mango", "apple", "peach", "pear", "strawberry"]
word = random.choice(word_list)

while True:
    guess = input("Enter a single letter: ")
    if len(guess) == 1 or guess.isalpha() == True:
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    
```

### Task 2: Check whether the guess is in the word

Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer.

Step 1: Create an if statement that checks if the guess is in the word.

Step 2: In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.

Step 3: Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.

```python
import random

word_list = ["mango", "apple", "peach", "pear", "strawberry"]
word = random.choice(word_list)

while True:
    guess = input("Enter a single letter: ")
    if len(guess) == 1 or guess.isalpha() == True:
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

Step 3: Move the code that you wrote to check if the guess is in the word into this function block.

The ask_for_input function.

Step 1: Define a function called ask_for_input.

Step 2: Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.

Step 3: Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.

Step 4: Outside the function, call the ask_for_input function to test your code.

```python
import random

word_list = ["mango", "apple", "peach", "pear", "strawberry"]
word = random.choice(word_list)

def check_guess(guess):
    """Function checks if a guess is in the target word or not.
    
    Args:
        guess (str): the letter that the user guesses is in the target word.
    """
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    """Function asks the user to guess a letter which might be in the target word.
    
    It also checks if the guess is a single letter. If not, it asks for input again.
    Only if a guess is in the target word it breaks from the while loop.
    
    The guess is then forwarded to check_guess function.
    """
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

## Milestone 4 - Create the Game class

### Task 1: Create the class

Create a new script called milestone_4.py. This file will contain the code for the third milestone.

Define the init method of the Hangman class.

Step 1: Create a class called Hangman.

Step 2: Inside the class, create an init method to initialise the attributes of the class. Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.

Step 3: Initialize the following attributes:

1.  **word**: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.

1.  **word_guessed**: list - A list of the letters of the word, with for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].

1.  **num_letters**: int - The number of UNIQUE letters in the word that have not been guessed yet.

1.  **num_lives**: int - The number of lives the player has at the start of the game.

1.  **word_list**: list - A list of words.

1.  **list_of_guesses**: list - A list of the guesses that have already been tried. Set this to an empty list initially.

```python
import random

class Hangman:
    """The Hangman class represents a game of Hangman.
    
    Attributes:
    -----------
    word_list : list of str
        A list of words from which the game chooses a word to be guessed.
    num_lives : int
        The number of lives a player has in the game (default = 5).
    word : str
        The randomly chosen word from word_list for the game.
    word_guessed : list of str
        A list of underscores representing the letters of the word that are not yet guessed.
    num_letters : int
        The number of unique letters in the word to be guessed.
    list_of_guesses : list of str
        A list of letters that have already been guessed by the player.
    """
    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new instance of the Hangman game.

        Parameters:
        -----------
        word_list : list of str
            A list of words from which the game chooses a word to be guessed.
        num_lives : int
            The number of lives a player has in the game (default = 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
```

### Task 2: Create methods for running the checks

In this task, you will create a method that will ask the user to guess a letter and another method that will check if the guess is in the word. Remember that a method is a function that is defined inside a class.

Step 1: Define a method called check_guess. Pass the guess to the method as a parameter. In the body of the method, write the code for the following steps:

1.  Convert the guessed letter to lower case

1.  Create an if statement that checks if the guess is in the word

1.  In the body of the if statement, print a message saying "Good guess! {guess} is in the word."

Step 2: Define a method called ask_for_input. In the body of the method, do the following:

1.  Create a while loop and set the condition to True.

1.  Ask the user to guess a letter and assign this to a variable called guess.

1.  Create an if statement that runs if the guess is NOT a single alphabetical character.

1.  In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."

1.  Create an elif statement that checks if the guess is already in the list_of_guesses.

1.  In the body of the elif statement, print a message saying "You already tried that letter!".

If the guess is a single alphabetical character and it's not already in the list_of_guesses:

1.  Create an else block and call the check_guess method. Remember to pass the guess as an argument to this method.

Finally, append the guess to the list_of_guesses. Ensure you do this in the else block of this function, rather than inside the check_guess method, so that the letter can be appended to the list_of_guesses in both conditions.

Step 3: Call the ask_for_input method to test your code.

```python
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
    
    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            #elif guess == "q":
                #break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

#a = Hangman(["apple", "orange"])
#a.ask_for_input()
```

### Task 3: Define what happens if the letter is in the word

Return to your check_guess method and extend it to replace the underscore(s) in the word_guessed with the letter guessed by the user. In the if block of your check_guess method, after your print statement, do the following:

Step 1: Create a for-loop that will loop through each letter in the word. Within the for-loop, do the following:

1. Create an <code>if</code> statement that checks if the letter is equal to the guess.
2. In the <code>if</code> block, replace the corresponding "_" in the <code>word_guessed</code> with the guess. 
HINT: You can index the <code>word_guessed</code> at the position  of the letter and assign it to the letter.
3. Outside the for-loop, reduce the variable num_letters by 1.

```python
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    guess_idx = self.word.index(guess)
                    self.word_guessed[guess_idx] = guess
            self.num_letters -= 1
    
    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            #elif guess == "q":
                #break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

#a = Hangman(["apple", "orange"])
#a.ask_for_input()
```

### Task 4: Define what happens if the letter is NOT in the word

Define what happens if the guess is not in the word you are trying to guess.

Step 1. In the check_guess method, Create an else statement.

Step 2: Within the else block:

1.  Reduce `num_lives' by 1.

1.  Print a message saying "Sorry, {letter} is not in the word."
1.  Print another message saying "You have {num_lives} lives left."

```python
import random

class Hangman:
    """The Hangman class represents a game of Hangman.
    
    Attributes:
    -----------
    word_list : list of str
        A list of words from which the game chooses a word to be guessed.
    num_lives : int
        The number of lives a player has in the game (default = 5).
    word : str
        The randomly chosen word from word_list for the game.
    word_guessed : list of str
        A list of underscores representing the letters of the word that are not yet guessed.
    num_letters : int
        The number of unique letters in the word to be guessed.
    list_of_guesses : list of str
        A list of letters that have already been guessed by the player.
    
    Methods:
    --------
    check_guess(guess):
        Checks if the given guess is in the word to be guessed and updates the game state accordingly.
        
    ask_for_input():
        Prompts the player to guess a letter and checks if the guess is valid.
        Updates the game state based on the guess until the player wins or loses.
    """
    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new instance of the Hangman game.

        Parameters:
        -----------
        word_list : list of str
            A list of words from which the game chooses a word to be guessed.
        num_lives : int
            The number of lives a player has in the game (default = 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        """
        Checks if the given guess is in the word to be guessed and updates the game state accordingly.
        If the guess is correct, the num_letters attribute is decreased by 1.
        If the guess is incorrect, the num_lives attribute is decreased by 1.
        
        Parameters:
        -----------
        guess : str
            The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    guess_idx = self.word.index(guess)
                    self.word_guessed[guess_idx] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        """
        Prompts the player to guess a letter and checks if the guess is valid.
        Updates the game state based on the guess until the player wins or loses.
        
        If a player uncovers all the letters in the word, there's no more underscores
        in the word_guessed attribute. If so, while loop is broken and game over.
        
        If the num_lives attribute reaches zero, the game is over and the player lost.
        
        If the player is neither won or lost, he is prompted to guess a letter, which is then checked
        if it's a single letter or not. If yes, letter is appended to the list_of_guesses attribute
        and forwarded to check_guess method. If not, the user is prompted to enter another letter.
        """
        while True:
            if "_" not in self.word_guessed:
                print(f"Congrats, you guessed the word {self.word}!")
                break
            elif self.num_lives == 0:
                print(f"Sorry, you ran out of lives and lost! Correct word was {self.word}. Better luck next time!")
                break
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

#a = Hangman(["pear"])
#a.ask_for_input()
```

## Milestone 5 - Putting it all together

### Task 1: Code the logic of the game

Create a function that will run all the code to run the game as expected. You should begin by creating a new script called milestone_5.py. Copy all the codes in milestone_4.py file into the newly created milestone_5.py file.

Step 1. Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps:

- Create a variable called num_lives and assign it to 5.

- Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game.

- Pass word_list and num_lives as arguments to the game object.

- Create a while loop and set the condition to True. In the body of the loop, do the following:

1.  Check if the <code>num_lives</code> is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'.
1.  Next, check if the <code>num_letters</code> is greater than 0. In this case, you would want to continue the game, so you need to call the <code>ask_for_input</code> method. 
1.  If the <code>num_lives</code> is not 0 and the <code>num_letters</code> is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'.

- Outside the function, call your play_game function to play your game. Don't forget to pass in your list of words as argument to the function.

```python
import random

class Hangman:
    """The Hangman class represents a game of Hangman.

    Attributes:
    -----------
    word_list : list of str
        A list of words from which the game chooses a word to be guessed.
    num_lives : int
        The number of lives a player has in the game (default = 5).
    word : str
        The randomly chosen word from word_list for the game.
    word_guessed : list of str
        A list of underscores representing the letters of the word that are not yet guessed.
    num_letters : int
        The number of unique letters in the word to be guessed.
    list_of_guesses : list of str
        A list of letters that have already been guessed by the player.
    
    Methods:
    --------
    check_guess(guess):
        Checks if the given guess is in the word to be guessed and updates the game state accordingly.
        
    ask_for_input():
        Prompts the player to guess a letter and checks if the guess is valid.
        Updates the game state based on the guess until the player wins or loses.
    """
    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new instance of the Hangman game.

        Parameters:
        -----------
        word_list : list of str
            A list of words from which the game chooses a word to be guessed.
        num_lives : int
            The number of lives a player has in the game (default = 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        """
        Checks if the given guess is in the word to be guessed and updates the game state accordingly.
        If the guess is correct, the num_letters attribute is decreased by 1.
        If the guess is incorrect, the num_lives attribute is decreased by 1.
        
        Parameters:
        -----------
        guess : str
            The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    guess_idx = self.word.index(guess)
                    self.word_guessed[guess_idx] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        """
        Prompts the player to guess a letter and checks if the guess is valid.
        Updates the game state based on the guess until the player wins or loses.
        
        If a player uncovers all the letters in the word, there's no more underscores
        in the word_guessed attribute. If so, while loop is broken and game over.
        
        If the num_lives attribute reaches zero, the game is over and the player lost.
        
        If the player is neither won or lost, he is prompted to guess a letter, which is then checked
        if it's a single letter or not. If yes, letter is appended to the list_of_guesses attribute
        and forwarded to check_guess method. If not, the user is prompted to enter another letter.
        """
        guess = input("Enter a single letter: ")
        if len(guess) != 1 or guess.isalpha() != True:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list):
    """
    Starts a new game of Hangman.

    Args:
    word_list (list): A list of words to be used as possible answers in the game.
    num_lives (int): The number of lives the player has (default=5)
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was: {game.word}.")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print(f"Congratulations, you won the game! The word was: {game.word}.")
            break

play_game(["apple", "pear", "peach"])
```

## Conclusion

This Hangman game was coded using a Hangman class object that was being called from the outside play_game function until the player loses or wins. A game is started by calling the play_game function with a list of words as the argument, upon which a random word is chosen for the game. Default number of lives is set to 5 inside the play_game function.

Outside play_game function includes a continuous while loop that continues to call the ask_for_input method inside an instance of Hangman class until the user wins the game or loses.

Hangman class is defined with various attributes that make up the heart of the game logic. Next, it includes two methods that make up the game progression. ask_for_input method prompts the user to guess a letter and verifies that the guess is actually a single letter. If these checks are passed, the guessed letter is forwarded to the check_guess method that evaluates the guess as correct or not. It then decreases the num_letters attribute if the guess is correct, or decreases the num_lives if it's not.
