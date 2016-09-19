#!/usr/bin/env python3

# I'm no fool, I made my code as spaghetti as possible to make it hard to read :D

import random
import skilstak.colors as c
import time

print(c.clear,end='')

input(c.base0 + "Welecome, if you're here you want me to read your mind.\nFirst, pick a random 2 digit number (10-99)\n\nPRESS ENTER TO CONTINUE")

print(c.clear,end='')

input(c.base0 + "Now that you have your number, subtract it's digits from itself.\n\nExaple: If your number was 41, do 41 - 4 - 1\n\nNow that subtracted number is your new number.\n\nPRESS ENTER TO CONTINUE")

print(c.clear,end='')

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','=','[',']','\\',';',"'",',','.','/','_','+','{','}','|',':','"','<','>','?','`','~']
assembly = ['line 12', 'line 31', 'line 17', 'line 4', 'line 19', 'line 20', 'line 1', 'line 28', 'line 11', 'line 9', 'line 20 again']

set = []

set.append(characters.pop(random.randint(0,91)))
set.append(characters.pop(random.randint(0,90)))
set.append(characters.pop(random.randint(0,89)))
set.append(characters.pop(random.randint(0,88)))
set.append(characters.pop(random.randint(0,87)))
set.append(characters.pop(random.randint(0,86)))
set.append(characters.pop(random.randint(0,85)))
set.append(characters.pop(random.randint(0,84)))
set.append(characters.pop(random.randint(0,83)))

symbol_table = 'Now remember your symbol that matches the new number.\n\n'
count = 0

for traceback in assembly:
  for item in set:
    count += 1
    if count == 1 or count == 2 or count == 3 or count == 4 or count == 5 or count == 6 or count == 7 or count == 8 or count == 9:
      symbol_table += '0' + str(count) + ':' + ' ' + item + '     '
    else:
      symbol_table += str(count) + ':' + ' ' + item + '     '
    if count == 11 or count == 22 or count == 33 or count == 44 or count == 55 or count == 66 or count == 77 or count == 88 or count == 99:
      symbol_table += '\n'
print(symbol_table)
input('PRESS ENTER TO CONTINUE')
print(c.clear)
answer = set.pop()

print(answer)