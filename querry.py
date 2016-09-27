#!/usr/bin/env python3
'''
Ask_int: 
  prompt: what message it will pull up. Example: What is your birthday?
  
  return_type (default 'int'): what type the function is going to return it as. Can be either 'str', 'int' or 'float'. 
  This does not mean what the input is going to be, the user still has to type a valid number in the prompt.
  
  blanking (default 0): what the input is going to be if you just hit enter on the prompt. Set to None if you don't want it to change.
  
  prompt_arrow (default c.base+'>>> '): where the person types their answer.
  
ask_options:
  prompt: what message it will pull up. Example: What are you doing for your birthday?
  
  options: the different things the person can choose from in their answer
  
  option_colors (default [c.random()]): the different colors the options will be. Will be in the same order as the options.
  If it runs out of colors, it will loop back around.
  
  increment_style (default 'numbers'): what the different option will distinguish themselves as.
  
  surround_style (default '()'): what the increment will be surrounded in. put only one character if you want the left side and
  the right side to be the same. Leave blank if you don't want the increment to be surrounded
  
  use_getch (default True): True means that it will use key detection, recomended with the alphabet incrment but it will work under
  circumstance.
  
  prompt_arrow (default c.base+'>>> '): where the person types their answer. Will only print if use_getch is False.
'''

import skilstak.colors as c
import getch

def ask_int(prompt,return_type='int',blanking=0,prompt_arrow=c.base3+'>>> '):
  while True:
    inp = input(prompt+'\n'+promp_arrow)
    if inp == '' and blanking != None:
      inp = blanking
    try:
      inp = float(inp)
      break
    except ValueError:
      continue
  if return_type == 'int':
    return int(inp)
  elif return_type == 'str':
    return str(inp)
  elif retun_type == 'float':
    return float(inp)

def put_in_letters(number,other_letters=''):
  import math
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  if number > 26:
    singled_number = number % 26
    number = math.floor(number / 26)
    other_letters = alphabet[singled_number-1] + other_letters
    put_in_letters(number,other_letters)
  else:
    return other_letters + alphabet[number-1]

def ask_options(prompt,options,option_colors=[c.random()],increment_style='numbers',surround_style='()',use_getch=True,prompt_arrow=c.base3+'>>> '):
  choices = 0
  for choice in options:
    choices += 1
  colors = []
  extended_colors = []
  for extend_color in options:
    for color in option_colors:
      extended_colors.append(color)
  
  new_options = []
  if increment_style = 'numbers':
    zeros = ''
    for digits in str(choices):
      zeros += '0'
    zeros = zeros[1:]
    for count in range(choice):
      count += 1
      new_options.append(extended_colors.pop(0) + surround_style[0] + zeros + str(count) + surround_style[1] + options.pop())
      
  elif increment_style = 'alphabet':
    for number in range(choices):
      number += 1
      letter = put_in_letter(choice)
      new_options.append(extended_colors.pop(0) + surround_style[0] + letter + surround_style[1] + options.pop())
  
  if use_getch:
    