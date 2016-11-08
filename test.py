#!/usr/bin/env python3
import skilstak.colors as c
import time

def clear():
  print(c.clear,end='')

clear()
name = input('What is your name?\n>>> ')
print('Your name is: ' + name)
