#!/usr/bin/env python3
import skilstak.colors as c
import random
from getch import getch
def clear():
  print(c.clear,end='')

def encrypt():
  clear()
  file_name = input('What file do you want encrypted (Note: this will not change the file, only output the encrypted form)?\n>>> ')
  text = open('/home/error404/side-projects/' + file_name)
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

def unencrypt():
  clear()
  file_name = input('What file do you want unencrypted (Not: this will not change the file, only out the unencrypted form)?\n>>> ')
  text = open('/home/error404/side-projects/' + file_name)
  clear()

  seed = ''
  for char in text:
    if char == '\x01':
      break
    seed += char

  seed = int(seed)
  random.seed(seed)

  unencrypted_message = ''
  for char in text:
    char = ord(char)
  unencrypted_message += chr(char + random.randint(1,char))

  with open('unencrypted_' + file_name[12:],'a+') as unencrypted_file:
    unencrypted_file.write(unencrypted_message[len(seed)+1:])

clear()

print("Hit 'e' to encrypt or 'u' to unencrypt.")
option = getch()

if option == 'e':
  encrypt()
elif option == 'u':
  unencrypt()
