#!/usr/bin/env python3
import skilstak.colors as c
from math import floor
def clear():
  print(c.clear + c.reset,end='')

while True:
  clear()
  try:
    choose_file = open('/home/error404/side-projects/' + input('What file would you like to play?\n>>> '))
    break
  except FileNotFoundError:
    pass

note_dict = {0:'C',1:'C#',2:'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',8:'G#',9:'A',10:'A#',11:'B'}

notes = []
for line in choose_file:
  for char in line:
    char = int(ord(char) % 128)
    notes.append('(Octave: ' + str(floor(char/12)-1) + ', Note: ' + note_dict[char % 12] + ')')

for note in notes:
  input(note)
