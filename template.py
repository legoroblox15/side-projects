#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='') 
  
def put_in_letters(number,other_letters=''):
  import math
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  if number > 26:
    singled_number = number % 26
    if singled_number == 0:
      singled_number == 1
    number = math.floor(number/26)
    other_letters = alphabet[singled_number-1] + other_letters
    return put_in_letters(number,other_letters)
  else:
    return alphabet[number-1] + other_letters

count = 0
while True:
  count += 1
  input(str(count) + ': ' + put_in_letters(count))