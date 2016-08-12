#!/usr/bin/env python3
import skilstak.colors as c
import random
def clear():
  print(c.clear,end='')

dungeon = [[' ' for x in range(10)] for y in range(10)]

exit_x = random.randint(0,9) 
exit_y = random.randint(0,9)

while True:
  p_x = random.randint(0,9)
  p_y = random.randint(0,9)
  if abs(p_x - exit_x) >= 5 or abs(p_y - exit_y) >= 5:
    break

dungeon[exit_y][exit_x] = c.green + '$' + c.base3
dungeon[p_y][p_x] = c.blue + '@' + c.base3


for count in range(40):
  while True:
    wall_x = random.randint(0,9)
    wall_y = random.randint(0,9)
    if dungeon[wall_y][wall_x] == ' ':
      dungeon[wall_y][wall_x] = c.red + '#'
      break
    else:
      continue
last_tile_rep = c.base3 + ' '
while True:
  clear()
  
  print(c.base3 + ' __________ ')
  for pr_y in dungeon:
    print(c.base3 + '|',end='')
    for pr_x in pr_y:
      print(pr_x,end='')
    print(c.base3 + '|')
  print(c.base3 + ' ---------- ')
  
  #print(str(p_x) + ', ' + str(p_y))
  mv = input('>>> ')
  if mv == 'w':
    try:
      if '#' not in dungeon[p_y-1][p_x] and p_y-1 >= 0:
        last_tile = dungeon[p_y-1][p_x]
        dungeon[p_y][p_x] = last_tile_rep
        last_tile_rep = last_tile
        p_y -= 1
        dungeon[p_y][p_x] = c.blue + '@'
    except IndexError:
      pass
  elif mv == 'a':
    try:
      if '#' not in dungeon[p_y][p_x-1] and p_x-1 >= 0:
        last_tile = dungeon[p_y][p_x-1]
        dungeon[p_y][p_x] = last_tile_rep
        last_tile_rep = last_tile
        p_x -= 1
        dungeon[p_y][p_x] = c.blue + '@'
    except IndexError:
      pass
  elif mv == 's':
    try:
      if '#' not in dungeon[p_y+1][p_x]:
        last_tile = dungeon[p_y+1][p_x]
        dungeon[p_y][p_x] = last_tile_rep
        last_tile_rep = last_tile
        p_y += 1
        dungeon[p_y][p_x] = c.blue + '@'
    except IndexError:
      pass
  elif mv == 'd':
    try:
      if '#' not in dungeon[p_y][p_x+1]:
        last_tile = dungeon[p_y][p_x+1]
        dungeon[p_y][p_x] = last_tile_rep
        last_tile_rep = last_tile
        p_x += 1
        dungeon[p_y][p_x] = c.blue + '@'
    except IndexError:
      pass