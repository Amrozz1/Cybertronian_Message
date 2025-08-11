import random 
with open("words.txt","r") as file:
    words = file.read().splitlines()

#print (words)

import numpy as np
wordly = np.array(words)
#print(wordly) faster
message = wordly[random.randint(0, len(wordly)-1)]
print(message)
trials = 6
i=0
while i < trials:
    guess = input(  "Enter a word ")
    if guess in wordly:
        if guess == message:
           print("You guessed the word!")
           break
        else:
           print("Try again!")
    else:
        print("Word not in list, try again!")
        i-=1