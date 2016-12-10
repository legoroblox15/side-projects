#!/usr/bin/env python3
import skilstak.colors as c
import random
from getch import getch
def clear():
  print(c.clear,end='')

def encrypt():
  clear()
  file_name = input('What file do you want encrypted (Note: this will not change the file, only output the encrypted form)?\n>>> ')
  try:
    text = open('/home/error404/side-projects/' + file_name)
  except FileNotFoundError:
    clear()
    print('Could not open file')
    return
  clear()

  values = []
  count = 0

  for line in text:
    for char in line:
      values.append(ord(char))
      count += 1

  random.seed(count)
  encrypted_message = ''

  for byte in values:
    encrypted_message += chr(byte + random.randint(1,byte))

  with open('encrypted_' + file_name,'a+') as encrypted_file:
    encrypted_file.write(str(count) + '\x01' + encrypted_message)
    encrypted_file.close()

def unencrypt():
  clear()
  file_name = input('What file do you want unencrypted (Not: this will not change the file, only out the unencrypted form)?\n>>> ')
  try:
    text = open('/home/error404/side-projects/' + file_name)
  except FileNotFoundError:
    clear()
    print('Could not open file')
    return
  clear()

  string_text = ''
  for line in text:
    string_text += line

  text = string_text
  text = text.split('\x01')
  seed = text.pop(0)
  text = text.pop()
  seed = int(seed)
  random.seed(seed)

  unencrypted_message = ''
  for char in text:
    char = ord(char)
  unencrypted_message += chr(char + random.randint(1,char))

  with open('unencrypted' + file_name[9:],'a+') as unencrypted_file:
    unencrypted_file.write(unencrypted_message)
    unencrypted_file.close()

clear()

print("Hit 'e' to encrypt or 'u' to unencrypt.")
option = getch()

if option == 'e':
  encrypt()
elif option == 'u':
  unencrypt()
