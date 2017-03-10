#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch
from os import environ
from re import sub

def clear():
  print(c.clear,end='')
clear()

def accuse(string,feed):
  print(feed,end='',flush=True)

  for letter in string:
    getch()
    print(letter,end='',flush=True)
  print()

cursor = c.base1 + environ['HOME'][6:] + 


print(cursor)
