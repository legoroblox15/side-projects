#!/usr/bin/env python3

import skilstak.colors as c
from getch import getch

def clear():
  print(c.clear,end='')

def game_has_not_been_beat_yet_do_not_worry_you_can_still_continue_giving_turns(board):
  for y in range(6):    #   Checks horizontal wins
    for x in range(3):
      if board[y][x] == board[y][x+1] == board[y][x+2] == board[y][x+3] == c.red + '█':
        return 'red'
      elif board[y][x] == board[y][x+1] == board[y][x+2] == board[y][x+3] == c.blue + '█':
        return 'blue'

  for y in range(2):    #   Checks vertical wins
    for x in range(7):
      if board[y][x] == board[y+1][x] == board[y+2][x] == board[y+3][x] == c.red + '█': 
        return 'red'
      elif board[y][x] == board[y+1][x] == board[y+2][x] == board[y+3][x] == c.blue + '█': 
        return 'blue'

  for y in range(2):    #   Checks upper left to lower right diagonal wins
    for x in range(3):
      if board[y][x] == board[y+1][x+1] == board[y+2][x+2] == board[y+3][x+3] == c.red + '█': 
        return 'red'
      elif board[y][x] == board[y+1][x+1] == board[y+2][x+2] == board[y+3][x+3] == c.blue + '█':
        return 'blue'

board = [[' ' for x in range(7)] for y in range(6)]
turn = 0

while True:
  clear()
  verdict = game_has_not_been_beat_yet_do_not_worry_you_can_still_continue_giving_turns(board)
  if verdict == 'red':
    clear()
    print(c.red + '█' + c.reset + ' Wins!'
    break
  elif verdict == 'blue':
    clear()
    print(c.blue + '█' + c.reset + ' Wins!'

  for y in board:
    print(c.base3 + '│',end='')
    for x in y:
      print(x,end='')
    print(c.base3 + '│')
  print(c.base3 + '├───────┤\n│1234567│')

  turn += 1
  if turn % 2 == 1:
    print('\n'+c.red+'█'+c.base3+"'s turn",end='')
    move = getch()
    if move == '\x1b':
      verdict = 'Hit escape (or the arrow keys idk because pygetch is a silly goose)'
      break
    
    elif move not in '1234567':
      turn -= 1
      continue
    
    if '█' in board[0][int(move)-1]:
      turn -= 1
      continue

    token = c.red + '█'

  else:
    print('\n'+c.blue+'█'+c.base3+"'s turn\n>>> ",end='')
    move = getch()
    if move == '\x1b':
      verdict = 'Hit escape (or the arrow keys idk because pygetch is a silly goose)'
      break
 
    elif move not in '1234567':
      turn -= 1
      continue

    if '█' in board[0][int(move)-1]:
      turn -= 1
      continue

    token = c.blue + '█'

  move = int(move) - 1
  for top in [5,4,3,2,1,0]:
    if board[top][move] == ' ':
      board[top][move] = token
      break
clear()
