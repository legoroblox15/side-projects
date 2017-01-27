#!/usr/bin/env python3
import skilstak.colors as c
import random
from getch import getch
from validwords import valid_words

def clear():
  print(c.clear,end='')

def print_board(history,letterboard):
  print('│' + history[19] + '│\t' + letterboard[a] + ' ' + letterboard[b] + ' ' + letterboard[c] + ' ' + letterboard[d] + ' ' + letterboard[e] + ' ' + letterboard[f]

words = valid_words()

history = ['       ' for line in range(20)]

