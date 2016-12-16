#!/usr/bin/env python3
import skilstak.colors as c
import getch
import json
def clear():
  print(c.clear,end='')

clear()

def login(password):
  for trys in range(3):
    print("-- FAKE TERMINAL, NOT THE ACTUALLY SYSTEM. PLEASE DO NOT TYPE IN YOUR REAL PASSWORD --")
    print('Password for admin@terminal.fake... ')
    typed_password = ''
    while True:
      key = getch.getch()
      if key == '\r': # "Enter" key
        if typed_password == password:
          return True
        else:
          clear()
          print('Permision Denied, Re-try ' + str(trys+1))
          break
      elif key == '\x7f': # "Backspace" key
        typed_password = typed_password[:-1]
      elif key == '\x1b' or key == '\x03' or key == '\x04' or key == '\x1a': # "Escape" key, Ctrl+C escape, Ctrl+D escape, Ctrl+Z escape.
        return False
      else:
        typed_password += key
  return False

def navigate():
  with open('/home/error404/side-projects/my-term/admin_data.json') as data:
    files = json.load(data)
    data.close()
  
  cursor = c.base1 + 'admin' + c.base01 + '@' + c.base00 + 'terminal:' + c.yellow + '~' + c.cyan + '$ '
  clear()
  command = input(cursor)
  
  if command.startswith('cd '):
    name = command.split(' ').pop()

if login('12345'):
  while True:
    navigate()
else:
  clear()
