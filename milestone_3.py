while True:
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")