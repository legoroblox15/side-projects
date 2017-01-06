#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch

def clear():
  print(c.clear,end='')

numb = 34
while True:
  clear()
  print(c.base3 + '"' + c.red + chr(numb-2) + c.base3 + '"\t"' + c.red + chr(numb-1) + c.base3 + '"\t"' + c.red + chr(numb) + c.base3 + '"\t"' + c.red + chr(numb+1) + c.base3 + '"\t"' + c.red + chr(numb+2) + c.base3 + '"')
  print(c.yellow + '\n\t\t'+str(numb)) 
  move = getch()
  if move == '.':
    numb += 1
  elif move == ',':
    numb -= 1
  elif move == ';':
    numb += 10
  elif move == 'l':
    numb -= 10
  elif move == '[':
    numb += 100
  elif move == 'p':
    numb -= 100
  elif move == '=':
    numb += 1000
  elif move == '-':
    numb -= 1000
  elif move == '\x1b':
    clear()
    break
  if numb < 34:
    numb = 34
  elif numb > 55293:
    numb = 55293
