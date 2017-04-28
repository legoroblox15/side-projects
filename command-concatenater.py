#!/usr/bin/env python3
import skilstak.colors as c

def clear():
  print(c.clear,end='')

def one_command():
  while True:
    clear()
    clearchoice = input(c.base3+ 'Welecome, this program will ask you for a list of commands and compile them into one command. It does this by spawning multiple Command Blocks on top of the Command Block you did the command in. When all of your commands are finnished, would you like to...\n\n'+c.red+'[1] Clear all Command Blocks (recommended).\n'+c.blue+'[2] Only clear the spawned Command Blocks.\n'+c.green+"[3] Only clear the original Command Block.\n"+c.yellow+"[4] Don't clear any Command Blocks.\n\n"+c.base01+'Input your desired choice to continue.\n>>> ')
    if clearchoice == '':
      clearchoice = '1'
    if clearchoice == '1' or clearchoice == '2' or clearchoice == '3' or clearchoice == '4':
      break
    
  commands = []

  while True:
    clear()
    try:
      print()
      command_numb = 0
      for pr_command in commands:
        command_numb += 1
        print(c.green + 'Command #' + str(command_numb) + ': ' + pr_command)
      print()
      command = input(c.base3 + "Now type your commands in the order you want them to be ran in. Hit Ctrl+D to undo your last command. Hit Ctrl+C when you have sent all of your commands.\n\n>>> /").strip()
      command = '/' + command
      if command != '/':
        commands.append(command)
    except KeyboardInterrupt:
      if commands != []:
        clear()
        break
    except EOFError:
      if commands != []:
        commands.pop()

  command_numb += 1

  if clearchoice == '1':
    commands.append('/fill ~ ~ ~ ~ ~-' + str(command_numb) + ' ~ air')
  elif clearchoice == '2':
    commands.append('/fill ~ ~ ~ ~ ~-' + str(command_numb - 1) + ' ~ air')
  elif clearchoice == '3':
    commands.append('/setblock ~ ~-' + str(command_numb) + ' ~ air')
  else:
    command_numb -= 1

  master = '/summon FallingSand ~ ~1 ~ {Time:1,Block:command_block,TileEntityData:{auto:1,Command:"'

  for command in commands:
    master += command + '"},Passengers:[{id:FallingSand,Time:1,Block:command_block,TileEntityData:{auto:1,Command:"'

  master = master[:-88]

  for bracket in range(command_numb-1):
    master += '}]'
  master += '}'
  print(master)
  input()

while True:
  clear()
  to_do = input(c.base3 + 'Greetings! This program will create very specialized and powerful command for you. Would you like to...\n' + c.red + '[1] Summon an entity.\n' + c.blue + '[2] Combined your commands into one giant .')
  if to_do == '1':
    pass
  elif to_do == '2':
    one_command()