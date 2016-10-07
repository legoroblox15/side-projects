#!/usr/bin/env python3
import skilstak.colors as c
import re
def clear():
  print(c.clear,end='')

while True:
  clear()
  solutions = []
  print(solutions)
  try:
    equation = input('>>> ')
  except KeyboardInterrupt:
    clear()
    break
  
  equation = re.sub(r'[^x0-9+-/*^ ]','',equation)
  input(equation)
  equation = re.sub(r'x','1x',equation)
  input(equation)
  equaiton = re.sub('\\^','**',equation)
  input(equation)
  for root in range(-101,101):
    substitute = re.sub(r'x','*'+str(root),equation)
    input(substitute)
    try:
      solved = eval(substitute)
      input(substitute)
    except SyntaxError:
      solutions = ['error']
      break
    if solved == 0:
      solutions.append(root)