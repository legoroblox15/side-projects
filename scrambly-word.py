#!/usr/bin/env python3
import skilstak.colors as c
from ask import ask
import random
def clear():
  print(c.clear,end='')
clear()

difficulty = ask('Difficulty (5-10)?', int, '>>> ', [5,6,7,8,9,10])
input(difficulty)
difficulty += 1
input(difficulty)











raise
clear()
with open('/home/error404/side-projects/words.txt') as words_file:
  words = words_file.read()
  words_file.close()

word_options = []

for word in words:
  if len(word) == difficulty:
    word_options.append(word)

input(word_options)
word = random.choice(word_options)

print(word)
