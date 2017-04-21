#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch
import os
from socket import gethostname

def clear():
  print(c.clear,end='')

def accuse(message,feed):
  print(feed,end='',flush=True)

  for letter in message:
    getch()
    print(letter,end='',flush=True)
  print()

def getlinefeed():
  return c.base1 + os.environ['HOME'][6:] + c.base00 + '@' + gethostname().split('.')[0] + ':' + c.yellow + os.path.split(os.getcwd())[1] + c.cyan + '$' + c.reset + ' '

if __name__ == '__main__':
  accuse('rm -rf *',getlinefeed())
  next_command = None

  while next_command != 'ls':
    next_command = input(getlinefeed()) 
    if next_command == 'ls':
      accuse('I AM IN CONTROL!',getlinefeed()+c.red)
    else:
      print(next_command.strip().split(' ')[0] + ': command not found')

