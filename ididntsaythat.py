#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch
import os
from socket import gethostname

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
  accuse('',getlinefeed())
