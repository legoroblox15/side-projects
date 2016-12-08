#!/usr/bin/env python3
import skilstak.colors as c
from re import sub
import random
def clear():
  print(c.clear,end='')

clear() 
numbs = input(c.cyan + 'Type the numbers and seperate them with commas.\n>>> ')
clear()

numb_range = input('Type the range.\n>>> ')

numbs = sub(r'[^0-9,]','',numbs).split(',')

numb_range = sub(r'[^0-9,]','',numb_range).split(',')

low = int(numb_range[0])
high = int(numb_range[1])

seed = ''
gen_numbs = []

try:
  while numbs != gen_numbs:
    if seed == '':
      seed = 0
    elif seed <= 0:
      seed = seed * -1
      seed += 1
    else:
      seed = seed * -1
    gen_numbs = []
    random.seed(seed)
    for count in numbs:
      gen_numbs.append(str(random.randint(low,high)))

except KeyboardInterrupt:
  clear()
  print('Terminated program after ' + str(abs(seed)*2+1) + ' Attempts.')
if numbs == gen_numbs:
  clear()
  print('Seed: ' + str(seed))
