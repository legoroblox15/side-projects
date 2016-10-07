#!/usr/bin/env python3
import skilstak.colors as c
import getch

def clear():
  print(c.clear,end='')

clear()
input(c.green + 'Hey! you want to play tic-toe-PRO (hippest name ever)?????\n'+c.base3+'>>> ')
while True:
  clear()
  print(c.yellow+'Great! So: are you playing with...' + c.magenta + '\n[1] an A.I' + c.blue + '\n[2] A human.' + c.base3 + '\n>>> ',end='')
  withp = getch.getch()
  if withp in ['1','2']:
    break
    
bts = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

running = True

while True:
  clear()
  board = bts[0] + '│' + bts[1] + '│' + bts[2] + '\n─┼─┼─\n' + bts[3] + '│' + bts[4] + '│' + bts[5] + '\n─┼─┼─\n' + bts[6] + '│' + bts[7] + '│' + bts[8]
  print("X's turn\n" + board)
  
  while True:
    x = getch.getch()
    if x == '\\':
      getch.pause_exit('')
    try:
      x = int(x)
    except ValueError:
      continue
    if x >= 1 and x <= 9 and bts[x-1] == ' ':
      bts[x-1] = 'x'
      break
    
  clear()
  board = bts[0] + '│' + bts[1] + '│' + bts[2] + '\n─┼─┼─\n' + bts[3] + '│' + bts[4] + '│' + bts[5] + '\n─┼─┼─\n' + bts[6] + '│' + bts[7] + '│' + bts[8]
  print("O's turn\n" + board)
  
  if withp == '1':
    aimove(bts)
  
  else:
    while True:
      o = getch.getch()
      if o == '\\':
        getch.pause_exit('')
      try:
        o = int(o)
      except ValueError:
        continue
      if o >= 1 and o <= 9 and bts[o-1] == ' ':
        bts[o-1] = 'o'
        break