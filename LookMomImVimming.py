#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch
import random
def clear():
  print(c.clear,end='')

clear()
command = None
commands = {c.yellow + '1 ' + c.base3 + 'Go to the end of this line!\r':'$'}
for test in commands:
  print(test)
  command = getch()
