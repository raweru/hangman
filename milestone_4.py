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
