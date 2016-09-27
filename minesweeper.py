#!/usr/bin/env python3
import skilstak.colors as c
import random
import colorama  
def clear():
  print(c.clear,end='')

def mc(x,y):
  return "\033["+str(y)+";"+str(x)+"H"

clear()
for x in range(20):
  for y in range(20):
    input(mc(x,y)+'Hello')
    clear()