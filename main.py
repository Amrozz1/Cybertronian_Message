import random 
with open("words.txt","r") as file:
    words = file.read().splitlines()

#print (words)

import numpy as np
wordly = np.array(words)
#faster
set_message = set(wordly)
#print(wordly) faster
message = wordly[random.randint(0, len(wordly)-1)]
print(message)
trials = 6
i=0
while i < trials:
    guess = input(  "Enter a word ")
    if guess in set_message:
        if guess == message:
           print("You guessed the word!")
           break
        else:
           print("Try again!")
           i+=1
    else:
        print("Word not in list, try again!")
        