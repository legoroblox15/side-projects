#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='')
clear()

try:
  input(c.green + 'Hey! you want to play tic-toe-PRO (hippest name ever)?????\n>>> ')
  while True:
    clear()
    opponent = input('Great! So: are you playing with...' + c.magenta + '\n[1] an A.I' + c.blue + '\n[2] A human.' + c.green + '\n>>> ')
    if opponent == '2' or opponent == '1':
      break
  
  clear()
  
  a = 'X'
  b = 'X'
  cc = 'X'
  d = 'X'
  e = 'X'
  f = 'X'
  g = 'X'
  h = 'X'
  i = 'X'
  
  board = a + ' |' + b + ' |' + cc + ' \n--+--+--\n' + d + ' |' + e + ' |' + f + ' \n--+--+--\n' + g + ' |' + h + ' |' + i 
  print(board)
  
except (KeyboardInterrupt, EOFError):
  clear()