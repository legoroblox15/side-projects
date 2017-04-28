#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch
import random

print(c.clear,end='',flush=True)

message = None

while message != '\x03':
  message = getch()
  print(c.random()+chr(random.randint(32,55195)),flush=True,end='')
