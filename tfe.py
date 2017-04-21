#!/usr/bin/env python3
import skilstak.colors as c
from random import randint
from random import choice
from getch import getch

def clear():
  print(c.clear,end='')

def eval_row(values):
  while c.base3 in values:
    values.remove(c.base3)
  
  new_row = []
  upgrade_color = {c.red:c.orange,c.orange:c.yellow,c.yellow:c.green,c.green:c.cyan,c.cyan:c.blue,c.blue:c.violet,c.violet:c.magenta,c.magenta:c.magenta}

  while len(values) > 1:
    if values[0] == values[1]:
      new_row.append(upgrade_color[values.pop(0)])
      del values[0]
    else:
      new_row.append(values.pop(0))
  
  if len(values) == 1:
    new_row.append(values.pop())
  
  while len(new_row) < 4:
    new_row.append(c.base3)

  return new_row  

def rotate_matrix(board):
  return [[board[0][c],board[1][c],board[2][c],board[3][c]] for c in range(4)]

def add_color(board):
  while True:
    y = randint(0,3)
    x = randint(0,3)
    if board[y][x] == c.base3:
      board[y][x] = choice([c.red, c.red, c.red, c.red, c.red, c.red, c.red, c.red, c.red, c.orange]) # 9:1 ratios is a 2048 standard
      return board

def pr_board(board):
  for row in board:
    for color in row:
      print(color + '■',end='')
    print()

def alive(board):
  return True

board = add_color(add_color([[c.base3 for x in range(4)] for y in range(4)]))

while alive(board):
  clear()
  pr_board(board)
  dirr = getch()

  old_board = board

  if dirr == '\x03':
    break
 
  elif dirr == 'h':
    board = [eval_row(row) for row in board]

  elif dirr == 'j':
    board = rotate_matrix([eval_row(row[::-1])[::-1] for row in rotate_matrix(board)])

  elif dirr == 'k':
    board = rotate_matrix([eval_row(row) for row in rotate_matrix(board)])
 
  elif dirr == 'l':
    board = [eval_row(row[::-1])[::-1] for row in board]

  if old_board != board:
    board = add_color(board)
  else:
    board = old_board
