#!/usr/bin/env python3
import skilstak.colors as c
import random
import time
import getch
from ask import ask

def clear():
  print(c.clear,end='')

def add_tiles(tile,count,dungeon,width,height):
  for adding in range(count):
    while True:
      y = random.randint(0,height-1)
      x = random.randint(0,width-1)
      if ' ' in dungeon[y][x]:
        dungeon[y][x] = tile
        break
  return dungeon

def set_path(width, height):
  tile_worth = 1/(width*height*(1/4))
  progress = 0
  path_tiles = [[0,0]]
  branches = [[0,0,None]]

  while branches != []:
    branch = random.choice(branches)
    branches.remove(branch)
    directions = [1,2,3,4]
    trials = 0
    while directions != []:
      trials += 1
      dir = random.choice(directions)
      directions.remove(dir)
      if dir == 1: # up
        if branch[0] == 0 or [branch[0]-2,branch[1]] in path_tiles or branch[2] == 'up':
          pass
        elif branch[0] == 1 or [branch[0]-3,branch[1]] in path_tiles:
          path_tiles.append([branch[0]-1,branch[1]])
          progress += tile_worth
        else:
          path_tiles.append([branch[0]-1,branch[1]])
          path_tiles.append([branch[0]-2,branch[1]])
          branches.append([branch[0]-2,branch[1],'up'])
          progress += tile_worth
          
      elif dir == 2: # right
        if branch[1] == width-1 or [branch[0],branch[1]+2] in path_tiles or branch[2] == 'right':
          pass
        elif branch[1] == width-2 or [branch[0],branch[1]+3] in path_tiles:
          path_tiles.append([branch[0],branch[1]+1])
          progress += tile_worth
        else:
          path_tiles.append([branch[0],branch[1]+1])
          path_tiles.append([branch[0],branch[1]+2])
          branches.append([branch[0],branch[1]+2,'right'])
          progress += tile_worth
            
      elif dir == 3: # down
        if branch[0] == height-1 or [branch[0]+2,branch[1]] in path_tiles or branch[2] == 'down':
          pass
        elif branch[0] == height-2 or [branch[0]+3,branch[1]] in path_tiles:
          path_tiles.append([branch[0]+1,branch[1]])
          progress += tile_worth
        else:
          path_tiles.append([branch[0]+1,branch[1]])
          path_tiles.append([branch[0]+2,branch[1]])
          branches.append([branch[0]+2,branch[1],'down'])
          progress += tile_worth
          
      elif dir == 4: # left
        if branch[1] == 0 or [branch[0],branch[1]-2] in path_tiles or branch[2] == 'left':
          pass
        elif branch[1] == 1 or [branch[0],branch[1]-3] in path_tiles:
          path_tiles.append([branch[0],branch[1]-1])
          progress += tile_worth
        else:
          path_tiles.append([branch[0],branch[1]-1])
          path_tiles.append([branch[0],branch[1]-2])
          branches.append([branch[0],branch[1]-2,'left'])
          progress += tile_worth

      clear()
      print(str(progress * 100)[:6] + '%')
  return path_tiles

def build_dungeon(width, height):
  darkness = c.base02
  dungeon = [[darkness + c.red + '█' for x in range(width)] for y in range(height)]
   
  path_tiles = set_path(width, height)

  for tile in path_tiles:
    dungeon[tile[0]][tile[1]] = ' '

  dungeon = add_tiles(c.base02 + c.green + '$',1,dungeon,width,height)
  
  dungeon = add_tiles(c.blue + '●',1,dungeon,width,height)
    
  return dungeon

def find_p(dungeon,width,height):
  for y_find in range(height):
    for x_find in range(width):
      if '●' in dungeon[y_find][x_find]:
        return [x_find,y_find]

def find_e(dungeon,width,height):
  for y_find in range(height):
    for x_find in range(width):
      if c.green + '$' in dungeon[y_find][x_find]:
        return [x_find,y_find]

def printing(dungeon,width,height):
  clear()
  tattle = 'It sure is dark'

  p_coords = find_p(dungeon,width,height)
  p_x = p_coords[0]
  p_y = p_coords[1]
  
  e_coords = find_e(dungeon,width,height)
  exit_x = e_coords[0]
  exit_y = e_coords[1]

  if p_x >= 1:
    dungeon[p_y][p_x-1] = dungeon[p_y][p_x-1].split(c.base02).pop() # left
    
  if p_x >= 1 and p_y >= 1:
    dungeon[p_y-1][p_x-1] = dungeon[p_y-1][p_x-1].split(c.base02).pop() # upper left
    
  if p_y >= 1:
    dungeon[p_y-1][p_x] = dungeon[p_y-1][p_x].split(c.base02).pop() # up  
    
  if p_x <= width-2 and p_y >= 1:
    dungeon[p_y-1][p_x+1] = dungeon[p_y-1][p_x+1].split(c.base02).pop() # upper right
    
  if p_x <= width-2:
    dungeon[p_y][p_x+1] = dungeon[p_y][p_x+1].split(c.base02).pop() # right
    
  if p_x <= width-2 and p_y <= height-2:
    dungeon[p_y+1][p_x+1] = dungeon[p_y+1][p_x+1].split(c.base02).pop() # lower right
    
  if p_y <= height-2:
    dungeon[p_y+1][p_x] = dungeon[p_y+1][p_x].split(c.base02).pop() # down
  
  if p_x >= 1 and p_y <= height-2:
    dungeon[p_y+1][p_x-1] = dungeon[p_y+1][p_x-1].split(c.base02).pop() # lower left
  
  corner_x = exit_x
  corner_y = p_y
  
  base = abs(p_x - corner_x)
  height = abs(exit_y - corner_y)
  
  left = base ** 2 + height ** 2
  hypo = round(left ** .5)
  hypo = hypo + random.randint(0,2) * random.choice([-1,1])
  if hypo < 0:
    hypo = 0
  
  if hypo <= 9:
    hypo = str(hypo) + ' '
  else:
    hypo = str(hypo)
  
  print(c.base3 + '┌─────────────────────────┐' )
  print(c.base3 + '│  Shattered Compass: ' + hypo + '  │')
  print(c.base3 + '├─────────────────────────┤')
  for pr_y in dungeon:
    print(c.base3 + '│',end='')
    for pr_x in pr_y:
      if c.base02 in pr_x:
        print(' ',end='')
      else:
        print(pr_x,end='')
    print(c.base3 + '│')
  print(c.base3 + '├─────────────────────────┤')
  print(c.base3 + '│'+c.base01+' *** '+tattle+' *** '+c.base3+'│') # Tattles need to be a total of 15 standard font width characters long
  print(c.base3 + '└─────────────────────────┘')
  return dungeon

def moving(dungeon,last_tile_rep,width,height):
  p_coords = find_p(dungeon,width,height)
  p_x = p_coords[0]
  p_y = p_coords[1]

  mv = getch.getch()

  if mv == '\x1b':
    return True
  
  elif mv == 'w':
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
    getch.pause('Fin.')
    return True
  return [dungeon,last_tile_rep]

if __name__ == '__main__':
  clear()
  width = 0
  height = 0
  while width <= 0 or height <= 0 or width * height < 2:
    width = ask('Please input the width of your dungeon',int)
    clear()
    height = ask('Please input the height of your dungeon',int)
    clear()
  dungeon = build_dungeon(width, height)
  last_tile_rep = c.base03 + '$'
  while True:
    dungeon = printing(dungeon,width,height)
    dungeon = moving(dungeon,last_tile_rep,width,height)
    if dungeon == True:
      break
    else:
      last_tile_rep = dungeon[1]
      dungeon = dungeon[0]
  clear()
