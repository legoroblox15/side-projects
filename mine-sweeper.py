#!/usr/bin/env python3
import skilstak.colors as c
import getch
import random
import math

def clear():
  print(c.clear,end='')
  
def build_grid(sx,sy,mines):
  grid = [['█' for x in range(sx)] for y in range(sy)]
  for mining in range(round(mines * (sx * sy))):
    while True:
      mine_x = random.randint(0,sx-1)
      mine_y = random.randint(0,sy-1)
      if c.base02 not in grid[mine_y][mine_x]:
        break
    grid[mine_y][mine_x] = c.base02 + grid[mine_y][mine_x]
    
  return grid

while True:
  clear()
  grid = build_grid(random.randint(1,25),random.randint(1,25),.3)
  for y in grid:
    for x in grid:
      print(x)
    print()
  print()
  input()