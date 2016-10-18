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
    
bts = ['1','2','3','4','5','6','7','8','9']

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
    if x >= 1 and x <= 9 and bts[x-1] and bts[x-1] in ['1','2','3','4','5','6','7','8','9']:
      bts[x-1] = c.red + 'x' + c.base3
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
      if o >= 1 and o <= 9 and bts[o-1] and bts[o-1] in ['1','2','3','4','5','6','7','8','9']:
        bts[o-1] = c.blue + 'o' + c.base3
        break