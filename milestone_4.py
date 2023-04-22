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
