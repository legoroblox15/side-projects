#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='')

table = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,"Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,"Sc":21,"Ti":22,"V":23,"Cr":24,"Mn":25,"Fe":26,"Co":27,"Ni":28,"Cu":29,"Zn":30,"Ga":31,"Ge":32,"As":33,"Se":34,"Br":35,"Kr":36,"Rb":37,"Sr":38,"Y":39,"Zr":40,"Nb":41,"Mo":42,"Tc":43,"Ru":44,"Rh":45,"Pd":46,"Ag":47,"Cd":48,"In":49,"Sn":50,"Sb":51,"Te":52,"I":53,"Xe":54,"Cs":55,"Ba":56,"La":57,"Ce":58,"Pr":59,"Nd":60,"Pm":61,"Sm":62,"Eu":63,"Gd":64,"Tb":65,"Dy":66,"Ho":67,"Er":68,"Tm":69,"Yb":70,"Lu":71,"Hf":72,"Ta":73,"W":74,"Re":75,"Os":76,"Ir":77,"Pt":78,"Au":79,"Hg":80,"Ti":81,"Pb":82,"Bi":83,"Po":84,"At":85,"Rn":86,"Fr":87,"Ra":88,"Ac":89,"Th":90,"Pa":91,"U":92,"Np":93,"Pu":94,"Am":95,"Cm":96,"Bk":97,"Cf":98,"Es":99,"Fm":100,"Md":101,"No":102,"Lr":103,"Rf":104,"Db":105,"Sg":106,"Bh":107,"Hs":108,"Mt":109}
have = {}

while True:
  clear()
  for ele in have:
    print(c.green + ele + c.orange + ' (' +str(table[ele]) + ')' + c.yellow + ': ' + c.red + str(have[ele]))
  try:
    command = input(c.base3 + '>>> ').strip()
  except (KeyboardInterrupt, EOFError):
    clear()
    break
  
  command = command.split(' ')
  times = command.pop()
  try:
    times = int(times)
    atom = command.pop()
    action = command.pop()
  except ValueError:
    if command == []:
      action = times
    else:
      atom = times
      action = command.pop()
    times = 1

  for count in range(times):
    if action == 'help':
      clear()
      print(c.base3+'"'+c.blue+'help'+c.base3+'":                                                           '+c.orange+' Pulls up this list (duh).')
      print(c.base3+'"'+c.blue+'clear'+c.base3+'":                                                          '+c.orange+' Clears your inventory.')
      print(c.base3+'"'+c.blue+'get/give (Element Symbol) [However many times]'+c.base3+'":                 '+c.orange+' Adds a specified element to your inventory')
      print(c.base3+'"'+c.blue+'discard/remove (Element Symbol) [However many times]'+c.base3+'":           '+c.orange+' Removes a specified element from your inventroy.')
      print(c.base3+'"'+c.blue+'fuse (Element Symbol)&(Element Symbol) [However many times]'+c.base3+'":    '+c.orange+' Fuses the 2 elements together into one element.')
      print(c.base3+'"'+c.blue+'split (Element Symbol) [However many times]'+c.base3+'":                    '+c.orange+' Spits the element into two other elements.\n')
      print(c.green + 'Any command that has "[However many times]" will default to one and is not required in the syntax.')
      try:
        input(c.base3 + 'Press enter to continue...')
      except (KeyboardInterrupt, EOFError):
        clear()
        break
    
    elif action == 'clear':
      have = {}
    
  
    elif action == 'get' or action == 'give':
      if atom in table and atom in have:
        have[atom] += 1
      elif atom in table:
        have[atom] = 1
      
    elif action == 'discard' or action == 'remove':
      if atom in have:
        if have[atom] != 0:
          have[atom] -= 1
          if have[atom] == 0:
            del have[atom]
          
    elif action == 'fuse':
      atom = atom.split('&')    # Ha Ha Ha 
      atom1 = atom.pop(0)
      atom2 = atom.pop()
      if atom1 in have and atom2 in have:
        if have[atom1] != 0 and have[atom2] != 0:
          total_mass = table[atom1] + table[atom2]
          if total_mass <= 109:
            for ele in table:
              if table[ele] == total_mass:
                have[atom1] -= 1
                if have[atom1] == 0:
                  del have[atom1]
                have[atom2] -= 1
                if have[atom2] == 0:
                  del have[atom2]
                if ele in have:
                  have[ele] += 1
                else:
                  have[ele] = 1
  
    elif action == 'split':
      if atom in have:
        if have[atom] != 0:
          have[atom] -= 1
          if have[atom] == 0:
            del have[atom]
          if table[atom] % 2 == 0:
            for ele in table:
              if table[ele] == table[atom] / 2:
                if ele in have:
                  have[ele] += 2
                else:
                  have[ele] = 2
          else:
            for ele in table:
              if table[ele] == table[atom] / 2 + .5:
                if ele in have:
                  have[ele] += 1
                else:
                  have[ele] = 1
            for ele in table:
              if table[ele] == table[atom] / 2 - .5:
                if ele in have:
                  have[ele] += 1
                else:
                  have[ele] = 1