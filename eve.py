#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='')

import random
import time

strat = [[50]]
strats = {}

gen = 0

while True:
  clear()
  
  bk_strat = strat
  temp = 'hot'
  won = False
  number = random.randint(1,100)
  
  print(c.blue+'Game: Okay, number set, guess away!')
  time.sleep(1)
  print(c.green+'Eve: Hmmm...')
  while True:
    time.sleep(1)
    if strat != []:
      if temp == 'hot':
        trial = strat.pop(0).pop(0) 
      elif temp == 'cold':
        trial = strat.pop().pop(0)
    else:
      print(c.green + 'Eve: I give up')
      time.sleep(1)
      print(c.blue + 'Game: The number was ' + str(number) + '.')
      break
    print(c.green + 'Eve: ' + str(trial) + '?')
    
    if trial == number:
      print(c.blue + 'Game: Correct!')
      time.sleep(1)
      print(c.green + 'Eve: I did it!')
      won = True
      break
    elif trial > number:
      print(c.blue + 'Game: Too hot!')
      temp = 'hot'
      print(c.green + 'Eve: Darn!')
    else:
      print(c.blue + 'Game: Too cold!')
      temp = 'cold'
      print(c.green + 'Eve: Darn!')
    closeness = abs(trial - number)
    