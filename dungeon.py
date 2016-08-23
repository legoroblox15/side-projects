#!/usr/bin/env python3
import skilstak.colors as c
import random
import time
def clear():
  print(c.clear,end='')

  

def build_dungeon():
  global dungeon
  
  dungeon = [[c.red + '#' for x in range(10)] for y in range(10)]
  
  exit_x = random.randint(0,9) 
  exit_y = random.randint(0,9)

  p_x = random.randint(0,9)
  p_y = random.randint(0,9)

  dungeon[p_y][p_x] = c.blue + '@' + c.base3

  path_tiles = [[p_y,p_x]]
  branches= [[p_y,p_x]]
  
  for branch in branches:
    print('Branching from branch ' + str(branch))
    dir = 1
    while True:
      # 1 = up, 2 = right, 3 = down, 4 = left
      if dir == 1: # up
        print('  Branching up...')
        if branch[0] == 0 or [branch[0]-2,branch[1]] in path_tiles:
          print('    Branch ' + str(branch) + ' Cannot go up.')
        elif branch[0] == 1 or [branch[0]-3,branch[1]]:
          print('    Branch ' + str(branch) + ' Can only go up one space.')
          path_tiles.append([branch[0]-1,branch[1]])
          branches.append([branch[0]-1,branch[1]])
        else:
          print('    Branch ' + str(branch) + ' Can go up two spaces.')
          path_tiles.append([branch[0]-1,branch[1]])
          path_tiles.append([branch[0]-2,branch[1]])
          branches.append([branch[0]-2,branch[1]])
            
      elif dir == 2: # right
        print('  Branching right...')
        if branch[1] == 9 or [branch[0],branch[1]+2] in path_tiles:
          print('    Branch ' + str(branch) + ' Cannot go right.')
        elif branch[1] == 8 or [branch[0],branch[1]+3] in path_tiles:
          print('    Branch ' + str(branch) + ' Can only go right one space.')
          path_tiles.append([branch[0],branch[1]+1])
          branches.append([branch[0],branch[1]+1])
        else:
          print('    Branch ' + str(branch) + ' Can go right two spaces.')
          path_tiles.append([branch[0],branch[1]+1])
          path_tiles.append([branch[0],branch[1]+2])
          branches.append([branch[0],branch[1]+2])
            
      elif dir == 3: # down
        print('  Branching down...')
        if branch[0] == 9 or [branch[0]+2,branch[1]] in path_tiles:
          print('    Branch ' + str(branch) + ' Cannot go down.')
        elif branch[0] == 8 or [branch[0]+3,branch[1]] in path_tiles:
          print('    Branch ' + str(branch) + ' Can only go down one space.')
          path_tiles.append([branch[0]+1,branch[1]])
          branches.append([branch[0]+1,branch[1]])
        else:
          print('    Branch ' + str(branch) + ' Can go down two spaces.')
          path_tiles.append([branch[0]+1,branch[1]])
          path_tiles.append([branch[0]+2,branch[1]])
          branches.append([branch[0]+2,branch[1]])
          
      elif dir == 4: # left
        print('  Branching left...')
        if branch[1] == 0 or [branch[0],branch[1]-2] in path_tiles:
          print('    Branch ' + str(branch) + ' Cannot go left.')
        elif branch[1] == 1 or [branch[0],branch[1]-3] in path_tiles:
          print('    Branch ' + str(branch) + ' Can only go left one space.')
          path_tiles.append([branch[0],branch[1]-1])
          branches.append([branch[0],branch[1]-1])
        else:
          print('    Branch ' + str(branch) + ' Can go left two spaces.')
          path_tiles.append([branch[0],branch[1]-1])
          path_tiles.append([branch[0],branch[1]-2])
          branches.append([branch[0],branch[1]-2])
      time.sleep(1)
      dir += 1
      if dir == 5:
        break

  for tile in path_tiles:
    dungeon[tile[0]][tile[1]] = c.base3 + ' '
  
  dungeon[path_tiles[-1][0]][path_tiles[-1][1]] = c.green + '$'
  
def moving():
  last_tile_rep = c.base3 + ' '
  while True:
    clear()
    for y_find in range(10):
      for x_find in range(10):
        if '@' in dungeon[y_find][x_find]:
          p_y = y_find
          p_x = x_find
          
    print(c.base3 + ' __________ ')
    for pr_y in dungeon:
      print(c.base3 + '|',end='')
      for pr_x in pr_y:
        print(pr_x,end='')
      print(c.base3 + '|')
    print(c.base3 + ' ---------- ')

    try:
      mv = input('>>> ')
    except EOFError:
      build_dungeon()
      continue
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
    if '$' in last_tile_rep:
      clear()
      input('Fin.')
      break
      
while True:
  build_dungeon()
  try:
    moving()
  except EOFError:
    build_dungeon
  except KeyboardInterrupt:
    break
clear()