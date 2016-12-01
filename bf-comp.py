#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch

def clear():
  print(c.clear,end='')

clear()
code = input()
clear()

memory = [0]
pointer = 0

def do_char(char,memory,pointer):
  if char == '+':
    memory[pointer] += 1
  elif char == '-' and memory[pointer] > 0:
    memory[pointer] -= 1
  elif char == '>':
    pointer += 1
    try:
      memory[pointer]
    except IndexError:
      memory.append(0)
  elif char == '<':
    pointer -= 1
    if pointer < 0:
      memory.insert(0,0)
  elif char == '.':
    try:
      print(chr(memory[pointer]),end='')
    except (OverflowError, ValueError):
      pass
  elif char == ',':
    memory[pointer] = ord(getch())
  return([memory,pointer])

for char in code:
  if char not in '[]':
    pack = do_char(char,memory,pointer)
    pointer = pack.pop()
    memory = pack.pop()
