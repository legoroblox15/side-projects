#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch
import os
from re import sub
from socket import gethostname

def clear():
  print(c.clear,end='')
clear()

def accuse(message,feed):
  print(feed,end='',flush=True)

  for letter in message:
    getch()
    print(letter,end='',flush=True)
  print()

cursor = c.base1 + os.environ['HOME'][6:] + c.base00 + '@' + gethostname().split('.')[0] + ':' + c.yellow + os.path.split(os.getcwd())[1] + c.cyan + '$' + c.reset + ' '

accuse('Chris Mason is my favorite student in the widest world!',cursor)
