#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='')

import random
import time

strat = []
strats = {}

gen = 0

def use_strat(strat):
  clear()
  
  bk_strat = strat
  temp = 'hot'
  number = random.randint(1,100)
  steps = 0
  trial = 201
  
  print(c.blue+'Game: Okay, number set, guess away!')
  time.sleep(1)
  print(c.green+'Eve: Hmmm... ' + str(strat))
  while True:
    steps += 1
    time.sleep(1)
    try:
      if temp == 'hot':
        trial = strat.pop(0).pop(0)
      elif temp == 'cold':
        trial = strat.pop().pop(0)
    except IndexError:
      print(c.green + 'Eve: I give up')
      time.sleep(1)
      print(c.blue + 'Game: The number was ' + str(number) + '.')
      return [bk_strat, steps, abs(trial - number)]
    print(c.green + 'Eve: ' + str(trial) + '?')
    
    if trial == number:
      print(c.blue + 'Game: Correct!')
      time.sleep(1)
      print(c.green + 'Eve: I did it!')
      return [bk_strat, steps, 0]
    elif trial > number:
      print(c.blue + 'Game: Too hot!')
      temp = 'hot'
      print(c.green + 'Eve: Darn!'+str(strat))
    else:
      print(c.blue + 'Game: Too cold!')
      temp = 'cold'
      print(c.green + 'Eve: Darn!')

use_strat(strat)