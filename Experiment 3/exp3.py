# hangman game

import random
word_list = ['python', 'java', 'swift', 'javascript', 'hangman']

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    print("Welcome to Hangman!")
    while attempts > 0:
        print("\nCurrent word:", display_word(word, guessed_letters))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        if guess in word:
            print("Good guess!")
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Incorrect guess.")
            guessed_letters.add(guess)
            attempts -= 1
        if attempts == 0:
            print(f"Sorry, you ran out of attempts. The word was: {word}")
            
hangman()