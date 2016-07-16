#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear,end='')
clear()
clearchoice = input(c.base0+ 'Welecome, this program will ask you for a list of commands and compile them into one command.\nIt does this by spawning more command blocks on top of the command block you did the command in.\nWhen all of your commands are finnished, would you like to...\n'+c.red+'[1] Clear your command blocks and the original command block (recommended)\n'+c.blue+'[2] Clear your command blocks but not the original command block'+c.green+"[3] Don't clear any command blocks\n"+c.magenta+'Input your desired message to continue.')
clear()
commands = []
while True:
  print(c.base0 + "Now type your commands in the order you want them to be ran in. Hit Ctrl+D to undo your last command. Hit Ctrl+C when you have sent all of your commands\n\n")