#!/usr/bin/env python3
roots = ['-thousand-','-million-','-billion-','-trillion-','-quadrillion-','-pintillion-','-sextillion-','-septillion-','-octillion-','-nonillion-','-decillion-','-undecillion-','-duodecillion-','-tredecillion-','-quattuorecillion-','-quinquadecillion-','-septendecillion-','-octodecillion-','-novendecillion-','-vigintillion-']
for n in range(21,1000):
  hund_roots = ['centi','ducenti','tricenti','quadringenti','quingenti','sescenti','septingenti','octingenti','nongenti']
  ten_roots = ['deci','viginti','triginta','quadraginta','quinquaginta','sexaginta','septuaginta','octoginta','nonaginta']
  one_roots = ['un','duo','tre','quattour','quinqua','se','septe','octo','nove']
  hundreds = '0'
  root = '-'
  n = str(n)
  digits = 0
  for blah in n:
    digits += 1
  if digits == 2:
    tens = n[:1]
    ones = n[-1:]
  else:
    hundreds = n[:1]
    tens = n[1:][:1]
    ones = n[-1:]
  if ones != '0':
    root += one_roots.pop(int(ones))
    if ones == '3' or ones == '6':
      if tens == '0':
        if hundreds == '1' or hundreds == '8':
          root += 's'
      else:
        if int(tens) >= 2 and int(tens) <= 5:
          root += 's'
    elif ones == '7' or ones == '9':
      if tens == '0':
        if hundred != '9':
          root += 'm'
      else:
        if tens != '9':
          root += 'm'
  if tens != '0':
    root += ten_roots.pop(int(tens)-1)
  if hundreds != '0':
    root += hund_roots.pop(int(hundreds)-1)
  roots.append(roots)
print(roots)