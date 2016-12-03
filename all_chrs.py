#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='')
clear()
for char in range(32,55296):
  print(chr(char),end='')
