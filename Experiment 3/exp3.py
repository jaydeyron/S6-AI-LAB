# hangman game

import random

words=["rajagiri", "school", "of", "engineering", "and", "technology"]
word=random.choice(words)
life=6
letters=set()
while life>0:
    print("\nLIFE : ","|"*life)
    print("Word :  ","".join(i if i in letters else "_" for i in word ))
    guess=input("Guess a letter : ")
    if guess in word:
        letters.add(guess)
    else:
        life-=1
        print("Wrong guess")
    if len(set(word))==len(letters):
        print("\nYou guessed the word : ",word)
        break
if life==0:
    print(f"Game over, the word was {word} ")