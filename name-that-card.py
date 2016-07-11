#!/usr/bin/env python3
running = True
running_two = True
while running:
  try:
    import random
    import skilstak.colors as c
    def clear():
      print(c.clear,end='')
    clear()
    try:
      print(c.base3 + 'Welecome to another Hearthstone program! If you want me to explain the rules, hit Ctrl+C, otherwise, hit Enter.')
      input('')
      running = False
    except KeyboardInterrupt:
      try:
        clear()
        print(c.yellow + 'Objective:  ' + c.green + 'The goal of the game is to list of as many cards as possible that fit in a ')
        print('            certain category. If you are with friends, then you can battle to see how ')
        print('            many cards each of you can list off!')
        print()
        print(c.yellow + 'Navigation: ' + c.green + 'To change the parameters the card has to follow, use the following commands;')
        print()
        print(c.cyan + '"spells":             ' + c.magenta + ' Toggles spells.')
        print(c.cyan + '"minions":            ' + c.magenta + ' Toggles minions.')
        print(c.cyan + '"weapons":            ' + c.magenta + ' Toggles weapons.')
        print(c.cyan + '"classic":            ' + c.magenta + ' Toggles Classic cards.')
        print(c.cyan + '"naxx":               ' + c.magenta + ' Toggles Shade of Naxxramus cards.')
        print(c.cyan + '"gvg":                ' + c.magenta + ' Toggles Goblins vs. Gnomes cards.')
        print(c.cyan + '"rock":               ' + c.magenta + ' Toggles Blackrock Mountain cards.')
        print(c.cyan + '"tgt":                ' + c.magenta + ' Toggles The Grand Tournament cards.')
        print(c.cyan + '"loe":                ' + c.magenta + ' Toggles League Of Explorers cards.')
        print(c.cyan + '"gods":               ' + c.magenta + ' Toggles Whispers of The Old Gods cards.')
        print(c.cyan + '"[Class Name]":       ' + c.magenta + " Toggles that class's class cards.")
        print(c.cyan + '"Neutral":            ' + c.magenta + ' Toggles Neutral cards.')
        print(c.cyan + '"[Number] mana":      ' + c.magenta + ' Toggles that mana cost.')
        print(c.cyan + '"[Number] attack":    ' + c.magenta + ' Toggles that attack value.')
        print(c.cyan + '"[Number] health":    ' + c.magenta + ' Toggles that health value.')
        print(c.cyan + '"basics":             ' + c.magenta + ' Toggles basic cards.')
        print(c.cyan + '"commons":            ' + c.magenta + ' Toggles common cards.')
        print(c.cyan + '"rares":              ' + c.magenta + ' Toggles rare cards.')
        print(c.cyan + '"epics":              ' + c.magenta + ' Toggles epic cards.')
        print(c.cyan + '"legendaries":        ' + c.magenta + ' Toggles legendary cards.')
        print(c.cyan + '"general":            ' + c.magenta + ' Toggles all minions without a subclass cards.')
        print(c.cyan + '"demons":             ' + c.magenta + ' Toggles all demons.')
        print(c.cyan + '"beasts":             ' + c.magenta + ' Toggles all beasts.')
        print(c.cyan + '"mechs":              ' + c.magenta + ' Toggles all mechs.')
        print(c.cyan + '"dragons":            ' + c.magenta + ' Toggles all dragons.')
        print(c.cyan + '"murlocs":            ' + c.magenta + ' Toggles all murlocs.')
        print(c.cyan + '"totems":             ' + c.magenta + ' Toggles all totems.')
        print()
        print(c.yellow + 'Side Note: The game will not start if no cards fit the parameters!')
        print(c.base01 + 'Hit Ctrl+D at anytime to stop the program.')
        input()
        continue
      except KeyboardInterrupt:
        continue
  except EOFError:
    try:
      clear()
      print(c.base3 + 'Hit Ctrl+D again to quit.')
      input()
    except EOFError:
      clear()
      print('Shutting down.')
      running = False
      running_two = False
    except KeyboardInterrupt:
      pass
f = c.red
t = c.base01

rules = {'sp':t,'mi':t,'we':t,'cls':t,'naxx':t,'gvg':t,'rock':t,'tgt':t,'loe':t,'gods':t,'druid':t,'hunter':t,'mage':t,'palidin':t,'priest':t,'rouge':t,'shaman':t,'warlock':t,'warrior':t,'neu':t,'m0':t,'m1':t,'m2':t,'m3':t,'m4':t,'m5':t,'m6':t,'m7':t,'m8':t,'m9':t,'m10':t,'m12':t,'m25':t,'a0':t,'a1':t,'a2':t,'a3':t,'a4':t,'a5':t,'a6':t,'a7':t,'a8':t,'a9':t,'a10':t,'a12':t,'h1':t,'h2':t,'h3':t,'h4':t,'h5':t,'h6':t,'h7':t,'h8':t,'h9':t,'h10':t,'h12':t,'h15':t,'b':t,'c':t,'r':t,'e':t,'l':t,'general':t,'demon':t,'beast':t,'mechs':t,'dragons':t,'murlocs':t,'totem':t}

while running_two:
  try:
    clear()
    print(rules['sp'] + 'Spells, ' + rules['mi'] + 'Minions, ' + rules['we'] + 'Weapons.                                                       ' + rules['general'] + 'General, ' + rules['demon'] + 'Demons, ' + rules['beast'] + 'Beasts, ' + rules['mechs'] + 'Mechs, ' + rules['dragons'] + 'Dragons, ' + rules['murlocs'] + 'Murlocs, ' + rules['totem'] + 'Totems')
    print()
    print(rules['cls'] + 'Classic, ' + rules['naxx'] + 'Shade of Naxxramus, ' + rules['gvg'] + 'Goblins vs. Gnomes, ' + rules['rock'] + 'Blackrock Mountain, ' + rules['tgt'] + 'The Grand Tournament, ' + rules['loe'] + 'League of Explorers, ' + rules['gods'] + 'Whispers of the Old Gods')
    print()
    print(rules['druid'] + 'Druid, ' + rules['hunter'] + 'Hunter, ' + rules['mage'] + 'Mage, ' + rules['palidin'] + 'Palidin, ' + rules['priest'] + 'Priest, ' + rules['rouge'] + 'Rouge, ' + rules['shaman'] + 'Shaman, ' + rules['warlock'] + 'Warlock, ' + rules['warrior'] + 'Warrior, ' + rules['neu'] + 'Neutral                 ' + rules['b'] + 'Basic, ' + rules['c'] + 'Commons, ' + rules['r'] + 'Rares, ' + rules['e'] + 'Epics, ' + rules['l'] + 'Legendaries')
    print()
    print(c.base3 + 'Mana: ' + rules['m0'] + '0, ' + rules['m1'] + '1, ' + rules['m2'] + '2, ' + rules['m3'] + '3, ' + rules['m4'] + '4, ' + rules['m5'] + '5, ' + rules['m6'] + '6, ' + rules['m7'] + '7, ' + rules['m8'] + '8, ' + rules['m9'] + '9, ' + rules['m10'] + '10, ' + rules['m12'] + '12, ' + rules['m25'] + '25\n\n' + c.base3 + 'Attack: ' + rules['a0'] + '0, ' + rules['a0'] + '0, ' + rules['a1'] + '1, ' + rules['a2'] + '2, ' + rules['a3'] + '4, ' + rules['a5'] + '5, ' + rules['a6'] + '6, ' + rules['a7'] + '7, ' + rules['a8'] + '8, ' + rules['a9'] + '9, ' + rules['a10'] + '10, ' + rules['a12'] + '12\n\n' + c.base3 + 'Health: ' + rules['h1'] + '1, ' + rules['h1'] + '1, ' + rules['h1'] + '1, ' + rules['h4'] + '4, ' + rules['h5'] + '5, ' + rules['h6'] + '6, ' + rules['h7'] + '7, ' + rules['h8'] + '8, ' + rules['h9'] + '9, ' + rules['h10'] + '10, ' + rules['h12'] + '12, ' + rules['h15'] + '15')
    set_rule = input(c.base3 + '>>> ')
    if set_rule in rules:
      print()
  except EOFError:
    try:
      clear()
      print(c.base3 + 'Hit Ctrl+D again to quit.')
      input('')
    except EOFError:
      clear()
      print('Shutting down.')
      running = False
      running_two = False
    except KeyboardInterrupt:
      pass
  except KeyboardInterrupt:
    pass
clear()