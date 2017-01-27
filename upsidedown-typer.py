#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch

def clear():
  print(c.clear,end='')

message = ''
char = None
while char != '\x1a' or char != '\x1b' or char != '\x03' or char == '\x04':
  clear()
  print(message,end='')
  char = getch()
  if char == '\x7f':
    message = message[1:]
  elif ord(char) >= 32:
    message += char
