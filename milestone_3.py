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