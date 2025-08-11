import random 
with open("words.txt","r") as file:
    words = file.read().splitlines()

#print (words)

import numpy as np
wordly = np.array(words)
#faster
set_message = set(wordly)
#print(wordly) faster

def pick_word():
    return wordly[random.randint(0, len(wordly)-1)]

def check_guess(guess, target):
    colors = []
    for i, ch in enumerate(guess):
        if ch == target[i]:
            colors.append("green")
        elif ch in target:
            colors.append("yellow")
        else:
            colors.append("gray")
    return colors