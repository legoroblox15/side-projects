#!/usr/bin/env python3

import skilstak.colors as c
from getch import getch

def clear():
  print(c.clear,end='')

def game_has_not_been_beat_yet_do_not_worry_you_can_still_continue_giving_turns(board):
  return True

board = [[' ' for x in range(7)] for y in range(6)]
turn = 0

while True:
  clear()
  verdict = game_has_not_been_beat_yet_do_not_worry_you_can_still_continue_giving_turns(board)
  if verdict != True:
    break
  
  for y in board:
    print(c.base3 + '│',end='')
    for x in y:
      print(x,end='')
    print(c.base3 + '│')
  print(c.base3 + '├───────┤\n│1234567│')

  turn += 1
  if turn % 2 == 1:
    print('\n'+c.red+'█'+c.base3+"'s turn\n>>> ",end='')
    move = getch()
    if move == '\x1b':
      verdict = 'Hit escape (or the arrow keys idk because pygetch is a silly goose)'
      break
    
    elif move not in '1234567':
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

    token = c.blue + '█'

  move = int(move) - 1
  for top in range(6,0):
    if board[top][move] == ' ':
      board[top][move] = token
      break
clear()
