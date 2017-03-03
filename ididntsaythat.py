#!/usr/bin/env python3
import skilstak.colors as c
from getch import getch
def clear():
  print(c.clear,end='')

def accuse(string,feed='>>> '):
  print(feed,end='',flush=True)

  for letter in string:
    getch()
    print(letter,end='',flush=True)
  print()

username = 'error404'
domain = 'skilstak'
path = 'side-projects'

accuse('rm -rf *', c.base1 + username + c.base01 + '@' + c.base00 + domain + ':' + c.yellow + path + c.cyan + '$' + c.reset + ' ')

