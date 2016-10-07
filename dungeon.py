#!/usr/bin/env python3
import skilstak.colors as c
import random
import time
import getch

def clear():
  print(c.clear,end='')

def add_tiles(tile,count,dungeon):
  for adding in range(count):
    while True:
      y = random.randint(0,24)
      x = random.randint(0,24)
      if ' ' in dungeon[y][x]:
        dungeon[y][x] = tile
        break
  return dungeon

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
  return path_tiles

def build_dungeon():
  darkness = c.base02
  dungeon = [[darkness + c.red + '█' for x in range(25)] for y in range(25)]
  
  path_tiles = set_path()
  
  total_tiles = -1
  for tile in path_tiles:
    dungeon[tile[0]][tile[1]] = c.base3 + ' '
    total_tiles += 1
  
  dungeon = add_tiles(c.base02 + c.green + '$',1,dungeon)
  
  dungeon = add_tiles(c.blue + '●',1,dungeon)
  
  dungeon = add_tiles(c.base02 + c.violet + '?', 10, dungeon)
    
  return dungeon

def riddle_door():
  clear()
  print(c.orange + 'You come across a wall that has strange runes on it, You can barely make out this pattern\n')
  coef = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
  b = random.randint(-6,6)
  blank = random.randint(1,5)
  answer = str(coef * blank + b)
  sequence = ''
  for x in range(1,6):
    if x == blank:
      sequence += '___  '
    else:
      sequence += str(coef * x + b) + '  '
  if input(sequence + '\n>>> ') == answer:
    clear()
    getch.pause('"You passed the test..." Echos the door.')
    clear()
    return True
  else:
    clear()
    getch.pause('The wall rummbles in dissaproval. you start to get dizzy! When the dizziness subsides you feel somewhere new...')
    clear()
    return False

def moving(dungeon):
  tattle = "It sure is dark"
  last_tile_rep = c.base03 + '$'
  for y_find in range(25):
    for x_find in range(25):
      if '●' in dungeon[y_find][x_find]:
        p_y = y_find
        p_x = x_find
        
  for y_find in range(25):
    for x_find in range(25):
      if c.green + '$' in dungeon[y_find][x_find]:
        exit_y = y_find
        exit_x = x_find
          
  while True:
    clear()
    if '?' in last_tile_rep:
      if riddle_door():  
        last_tile_rep = ' '
      else:
        while True:
          x_new = random.randint(0,24)
          y_new = random.randint(0,24)
          if ' ' in dungeon[y_new][x_new]:
            break
          dungeon[p_y][p_x] = last_tile_rep
          p_x = x_new
          p_y = y_new
          dungeon[p_y][p_x] = c.blue + '●'
          last_tile_rep = ' '
            
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
    
    corner_x = exit_x
    corner_y = p_y
    
    base = abs(p_x - corner_x)
    height = abs(exit_y - corner_y)
    
    
    left = base ** 2 + height ** 2
    hypo = round(left ** .5)
    hypo = hypo + random.randint(0,4) * random.choice([-1,1])
    if hypo < 0:
      hypo = 0
    
    if hypo <= 9:
      hypo = str(hypo) + ' '
    else:
      hypo = str(hypo)
    
    print(c.base3 + '┌─────────────────────────┐')
    print(c.base3 + '│  Shattered Compass: '+hypo+'  │')
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
    print(c.base3 + '│'+c.base01+' *** '+tattle+' *** '+c.base3+'│') # Tattles need to be a total of 15 standard font widthed characters long
    print(c.base3 + '└─────────────────────────┘')
    mv = getch.getch()
    
    if mv == 'x':
      return False
    
    elif mv == 'n':
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

  
while True:
  dungeon = build_dungeon()
  staying = moving(dungeon)
  if not staying:
    break
clear()