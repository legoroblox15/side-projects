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
    
  return dungeon

def printing(dungeon):
  tattle = "It sure is dark"
  cheat_codes = ''
  debug = ['' for blank in range(31)]
  debugging = False
  mv = ''
  clip = True

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
    hypo = hypo + random.randint(0,2) * random.choice([-1,1])
    if hypo < 0:
      hypo = 0
    
    if hypo <= 9:
      hypo = str(hypo) + ' '
    else:
      hypo = str(hypo)
    
    if len(cheat_codes) == 10:
      cheat_codes = cheat_codes[1:] + mv
    else:
      cheat_codes += mv

    if cheat_codes == 'GENESIS1:3':
      for y in range(25):
        for x in range(25):
          dungeon[y][x] = dungeon[y][x].split(c.base02).pop()

    elif cheat_codes == 'MAKEITDARK':
      for y in range(25):
        for x in range(25):
          if not dungeon[y][x].startswith(c.base02):
            dungeon[y][x] = c.base02 + dungeon[y][x]

    elif cheat_codes == 'IHATEDOORS':
      for y in range(25):
        for x in range(25):
          if '?' in dungeon[y][x]:
            dungeon[y][x] = ' '

    elif cheat_codes == 'DEBUGSTUFF':
      if debug != ['' for blank in range(31)]:
        debug = ['' for blank in range(31)]
        debugging = False
      else:
        debugging = True

    elif cheat_codes == 'NOMASWALLS':
      if clip:
        clip = False
      else:
        clip = True

    elif cheat_codes == 'WARPTOSPOT':
      try:
        x_warp = int('X value?\n>>> ')
        y_warp = int('Y value?\n>>> ')
        dungeon[p_y][p_x] = last_tile_rep
        last_tile_rep = dungeon[y_warp][x_warp]
        dungeon[y_warp][x_warp] = c.blue + '●'
        p_x = x_warp
        p_y = y_warp
        cheat_codes = '##########'
        continue
      except ValueError:
        pass

    if debugging:
      debug[0] = c.blue + '	Player Coordinates: (' + str(p_x) + ', ' + str(p_y) + ')'
      debug[1] = c.blue + '	Tile Standing On: "' + last_tile_rep + c.blue + '"' 
      debug[2] = c.blue + '	Cheat Code Keylogger: "' + cheat_codes + c.blue + '"'       
      debug[3] = c.blue + '	Clipping: ' + str(clip)
      debug[4] = c.blue + '	Debugging: ' + str(debugging) 	

    print(c.base3 + '┌─────────────────────────┐' + debug[0])
    print(c.base3 + '│  Shattered Compass: ' + hypo + '  │' + debug[1])
    print(c.base3 + '├─────────────────────────┤' + debug[2])
    debug_iter = 2
    for pr_y in dungeon:
      debug_iter += 1
      print(c.base3 + '│',end='')
      for pr_x in pr_y:
        if c.base02 in pr_x:
          print(' ',end='')
        else:
          print(pr_x,end='')
      print(c.base3 + '│' + debug[debug_iter])
    print(c.base3 + '├─────────────────────────┤' + debug[28])
    print(c.base3 + '│'+c.base01+' *** '+tattle+' *** '+c.base3+'│' + debug[29]) # Tattles need to be a total of 15 standard font width characters long
    print(c.base3 + '└─────────────────────────┘' + debug[30])
    return dungeon

def moving(dungeon)
    mv = getch.getch()

    if mv == '\x1b':
      return False
    
    elif mv == 'n':
      return True
    
    elif mv == 'w':
      try:
        if '█' not in dungeon[p_y-1][p_x] and p_y-1 >= 0 or clip == False:
          last_tile = dungeon[p_y-1][p_x]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_y -= 1
          dungeon[p_y][p_x] = c.blue + '●'
      except IndexError:
        pass
    elif mv == 'a':
      try:
        if '█' not in dungeon[p_y][p_x-1] and p_x-1 >= 0 or clip == False:
          last_tile = dungeon[p_y][p_x-1]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_x -= 1
          dungeon[p_y][p_x] = c.blue + '●'
      except IndexError:
        pass
    elif mv == 's':
      try:
        if '█' not in dungeon[p_y+1][p_x] or clip == False:
          last_tile = dungeon[p_y+1][p_x]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_y += 1
          dungeon[p_y][p_x] = c.blue + '●'
      except IndexError:
        pass
    elif mv == 'd':
      try:
        if '█' not in dungeon[p_y][p_x+1] or clip == False:
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

if __name__ == '__main__':
  staying == True
  while True:
    if staying == False:
      break
    dungeon = build_dungeon()
    while True:
      printing(dungeon)
      staying = moving(dungeon)
      if staying == False:
        break
  clear()
