import random

life=6
words=["rajagiri", "school", "of", "engineering", "and", "technology"]
word=random.choice(words)
letters=set()
while life>0:
    print("LIFE: ","|"*life)
    print("Word: ","".join(i if i in letters else "_" for i in word))
    guess=input("Guess a letter: ")
    if guess in letters:
        print("Already guessed, try again")
        continue
    if guess in word:
        letters.add(guess)
    else:
        life-=1
        print("Wrong guess")
    if len(set(word))==len(letters):
        print(f"You guessed the word: {word}")
        break
if life==0:
    print(f"You lost! The word was {word}")