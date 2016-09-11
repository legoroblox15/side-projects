#!/usr/bin/env python3
import skilstak.colors as c
import random
import time

def clear():
  print(c.clear,end='')

def set_path():  
  seed_x = random.randint(0,24)
  seed_y = random.randint(0,24)
  
  path_tiles = [[seed_x,seed_y]]
  branches = [[seed_x,seed_y,None]]
  
  while True:
    branch = random.choice(branches)
    branches.remove(branch)
    directions = [1,2,3,4]
    expanded = False
    trials = 0
    while True:
      trials += 1
      dir = random.choice(directions)
      directions.remove(dir)
      if dir == 1: # up
        if branch[0] == 0 or [branch[0]-2,branch[1]] in path_tiles or branch[2] == 'up':
          pass
        elif branch[0] == 1 or [branch[0]-3,branch[1]] in path_tiles:
          path_tiles.append([branch[0]-1,branch[1]])
          expanded = True
        else:
          path_tiles.append([branch[0]-1,branch[1]])
          path_tiles.append([branch[0]-2,branch[1]])
          branches.append([branch[0]-2,branch[1],'up'])
          expanded = True
          
      elif dir == 2: # right
        if branch[1] == 24 or [branch[0],branch[1]+2] in path_tiles or branch[2] == 'right':
          pass
        elif branch[1] == 23 or [branch[0],branch[1]+3] in path_tiles:
          path_tiles.append([branch[0],branch[1]+1])
          expanded = True
        else:
          path_tiles.append([branch[0],branch[1]+1])
          path_tiles.append([branch[0],branch[1]+2])
          branches.append([branch[0],branch[1]+2,'right'])
          expanded = True
            
      elif dir == 3: # down
        if branch[0] == 24 or [branch[0]+2,branch[1]] in path_tiles or branch[2] == 'down':
          pass
        elif branch[0] == 23 or [branch[0]+3,branch[1]] in path_tiles:
          path_tiles.append([branch[0]+1,branch[1]])
          expanded = True
        else:
          path_tiles.append([branch[0]+1,branch[1]])
          path_tiles.append([branch[0]+2,branch[1]])
          branches.append([branch[0]+2,branch[1],'down'])
          expanded = True
          
      elif dir == 4: # left
        if branch[1] == 0 or [branch[0],branch[1]-2] in path_tiles or branch[2] == 'left':
          pass
        elif branch[1] == 1 or [branch[0],branch[1]-3] in path_tiles:
          path_tiles.append([branch[0],branch[1]-1])
          expanded = True
        else:
          path_tiles.append([branch[0],branch[1]-1])
          path_tiles.append([branch[0],branch[1]-2])
          branches.append([branch[0],branch[1]-2,'left'])
          expanded = True
      if directions == []:
        break
    if branches == []:
      break
  return [path_tiles,branches]

def build_dungeon():
  darkness = ''
  dungeon = [[darkness + c.red + '█' for x in range(25)] for y in range(25)]
  
  path_tiles = set_path()
  branches = path_tiles.pop()
  path_tiles = path_tiles.pop()
    
  for tile in path_tiles:
    dungeon[tile[0]][tile[1]] = c.base3 + ' '
  
  dungeon[path_tiles[-1][0]][path_tiles[-1][1]] = darkness + c.green + '$'
  while True:
    start = random.choice(path_tiles)
    if start != [path_tiles[-1][0],path_tiles[-1][1]]:
      break
  dungeon[start[0]][start[1]] = c.blue + '●'
  
  path_count = -1
  for tile in path_tiles:
    path_count += 1
  
  colors = [c.yellow, c.magenta, c.violet, c.blue, c.cyan, c.green, c.base00, c.base01] 
  for color in colors:
    while True:
      key = random.randint(0,path_count)
      door = random.randint(key+1,path_count)
      if ' ' in dungeon[path_tiles[key][0]][path_tiles[key][1]] and ' ' in dungeon[path_tiles[door][0]][path_tiles[door][1]]:
        dungeon[path_tiles[key][0]][path_tiles[key][1]] = darkness + color + '%'
        dungeon[path_tiles[door][0]][path_tiles[door][1]] = darkness + colors + '&'

  return dungeon
  
def moving(dungeon):
  tattle = "It sure is dark"
  last_tile_rep = c.base03 + '$'
  for y_find in range(25):
    for x_find in range(25):
      if '●' in dungeon[y_find][x_find]:
        p_y = y_find
        p_x = x_find
          
  while True:
    clear()
    if p_x >= 1:
      dungeon[p_y][p_x-1] = dungeon[p_y][p_x-1].split(c.base02).pop() # left
      
    if p_x >= 1 and p_y >= 1:
      dungeon[p_y-1][p_x-1] = dungeon[p_y-1][p_x-1].split(c.base02).pop() # upper left
      
    if p_y >= 1:
      dungeon[p_y-1][p_x] = dungeon[p_y-1][p_x].split(c.base02).pop() # up  
      
    if p_x <= 23 and p_y >= 1:
      dungeon[p_y-1][p_x+1] = dungeon[p_y-1][p_x+1].split(c.base02).pop() # upper right
      
    if p_x <= 23:
      dungeon[p_y][p_x+1] = dungeon[p_y][p_x+1].split(c.base02).pop() # right
      
    if p_x <= 23 and p_y <= 23:
      dungeon[p_y+1][p_x+1] = dungeon[p_y+1][p_x+1].split(c.base02).pop() # lower right
      
    if p_y <= 23:
      dungeon[p_y+1][p_x] = dungeon[p_y+1][p_x].split(c.base02).pop() # down
    
    if p_x >= 1 and p_y <= 23:
      dungeon[p_y+1][p_x-1] = dungeon[p_y+1][p_x-1].split(c.base02).pop() # lower left
  
    print(c.base3 + '┌─────────────────────────┐')
    for pr_y in dungeon:
      print(c.base3 + '│',end='')
      for pr_x in pr_y:
        if c.base02 in pr_x:
          print(' ',end='')
        else:
          print(pr_x,end='')
      print(c.base3 + '│')
    print(c.base3 + '├─────────────────────────┤')
    print(c.base3 + '│'+c.base01+' *** '+tattle+' *** '+c.base3+'│') # Tattles need to be a total of 15 standard font widthed characters long
    print(c.base3 + '└─────────────────────────┘')

    try:
      mv = input('>>> ')
    except EOFError:
      build_dungeon()
      continue
    if mv == 'w':
      try:
        if '█' not in dungeon[p_y-1][p_x] and p_y-1 >= 0:
          last_tile = dungeon[p_y-1][p_x]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_y -= 1
          dungeon[p_y][p_x] = c.blue + '●'
      except IndexError:
        pass
    elif mv == 'a':
      try:
        if '█' not in dungeon[p_y][p_x-1] and p_x-1 >= 0:
          last_tile = dungeon[p_y][p_x-1]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_x -= 1
          dungeon[p_y][p_x] = c.blue + '●'
      except IndexError:
        pass
    elif mv == 's':
      try:
        if '█' not in dungeon[p_y+1][p_x]:
          last_tile = dungeon[p_y+1][p_x]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_y += 1
          dungeon[p_y][p_x] = c.blue + '●'
      except IndexError:
        pass
    elif mv == 'd':
      try:
        if '█' not in dungeon[p_y][p_x+1]:
          last_tile = dungeon[p_y][p_x+1]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_x += 1
          dungeon[p_y][p_x] = c.blue + '●'
      except IndexError:
        pass
    if c.green + '$' in last_tile_rep:
      clear()
      input('Fin.')
      break

  
while True:
  dungeon = build_dungeon()
  try:
    moving(dungeon)
  except KeyboardInterrupt:
    break
clear()