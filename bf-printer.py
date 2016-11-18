#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch

def clear():
  print(c.clear,end='')

clear()
message = input()

mem_values = []
while message != '':
  char = message[:1]
  message = message[1:]
  if char == '\\':
    char += message[:1]
    message = message[1:]
    if char == '\\n':
      mem_values.append(10)
    elif char == '\\t':
      mem_values.append(9)
    elif char == '\\\\':
      mem_values.append(92)
    elif char == '\\x':
      char = ''
      while message[:1] in '1234567890' and message[:1] != '':
        char += message[:1]
        message = message[1:]
      if char != '':
        mem_values.append(int(char))
  else:
    mem_values.append(ord(char))
print(mem_values)
