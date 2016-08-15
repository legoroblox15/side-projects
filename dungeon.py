#!/usr/bin/env python3
import skilstak.colors as c
import random
def clear():
  print(c.clear,end='')

dungeon = [[' ' for x in range(10)] for y in range(10)]

exit_x = random.randint(0,9) 
exit_y = random.randint(0,9)


p_x = random.randint(0,9)
p_y = random.randint(0,9)

path_corner_x = p_x
path_corner_y = p_y

dungeon[p_y][p_x] = c.blue + '@' + c.base3

path_tiles = []
dir = None

for lines in range(random.randint(4,8)):
  while True:
    prev_dir = dir
    while True:
      dir = random.randint(1,4)
      if dir == prev_dir:
        continue
      elif dir += 2 == prev_dir or dir -= 2 == prev_dir:
        continue:
      else:
        break
    
    if dir == 1:
      if path_corner_x == 9:
        continue
      else:
        length = random.randint(1, 9 - path_corner_x)
        for path in range(length):
          path_corner_x += 1
          
          path_tiles.append([path_corner_y, path_corner_x])
    
    elif dir == 2:
      if path_corner_y == 9:
        continue
      else:
        length = random.randint(1, 9 - path_corner_y)
        for path in range(length):
          path_corner_y += 1
          path_tiles.append([path_corner_y, path_corner_x])
    
    elif dir == 3:
      if path_corner_x == 0:
        continue
      else:
        length = random.randint(1, path_corner_x)
        for path in range(length):
          path_corner_x -= 1
          path_tiles.append([path_corner_y, path_corner_x])
    
    elif dir == 4:
      if path_corner_y == 0:
        continue
      else:
        length = random.randint(1, path_corner_y)
        for path in range(length):
          path_corner_y -= 1
          path_tiles.append([path_corner_y, path_corner_x])
    break

dungeon[path_tiles[-1][0]][path_tiles[-1][1]] = c.green + '$'
        
for count in range(40):
  while True:
    wall_x = random.randint(0,9)
    wall_y = random.randint(0,9)
    if [wall_y, wall_x] in path_tiles:
      continue
    if dungeon[wall_y][wall_x] == ' ':
      dungeon[wall_y][wall_x] = c.red + '#'
      break
    else:
      continue
  
last_tile_rep = c.base3 + ' '

def debug():
  print(c.base3 + 'Player: ' + str(p_x) + ', ' + str(p_y))
  print(c.base3 + 'Exit: ' + str(exit_x) + ', ' + str(exit_y))
  
  for tile in path_tiles:
    if ' ' in dungeon[tile[0]][tile[1]]:
      dungeon[tile[0]][tile[1]] = c.yellow + '^'
      
while True:
  clear()
  debug()
  
  print(c.base3 + ' __________ ')
  for pr_y in dungeon:
    print(c.base3 + '|',end='')
    for pr_x in pr_y:
      print(pr_x,end='')
    print(c.base3 + '|')
  print(c.base3 + ' ---------- ')
  
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