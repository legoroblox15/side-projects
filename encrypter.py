#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='')

clear()
text = open('/home/error404/side-projects/' + input('What file do you want encrypted (Note: this will not change the file, only output the encrypted form)?\n>>> '))
clear()

values = []
count = 0

for line in text:
  for char in line:
    values.append(ord(char))
    count += 1


