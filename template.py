#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='')
from getch import getch
test = getch()
print(test)