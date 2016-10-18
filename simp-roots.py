#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='')

while True:
  clear()
  radicant = input("What's in the radical? It better be radical\n>>> √")
  try:
    radicant = int(radicant)
  except ValueError:
    continue
  break

if radicant < 0:
  radicant = radicant * -1
  i = 'i'
else:
  i = ''
base = 1
squares = []

while (base+1)**2 <= radicant:
  base += 1
  squares.insert(0,base**2)

found = False
for square in squares:
  if radicant/(square**.5) == square**.5:
    print('±' + str(int(square ** .5)) + i)
    found = True
    break
  elif radicant % square == 0:
    print('±' + str(int(square ** .5)) + i + '√' + str(int(radicant/square)))
    found = True
    break

if not found:
  print('±' + i + '√' + str(int(radicant)))