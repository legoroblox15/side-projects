#!/usr/bin/env python3
def trolling(username,domain,path):
  import skilstak.colors as c
  import time
  import re
  import signal
  def handler(signum, frame):
    pass # <-- code here
  signal.signal(signal.SIGTSTP, handler) 
  time.sleep(2)
  cursor = c.base1 + username + c.base01 + '@' + c.base00 + domain + ':' + c.yellow + path + c.cyan + '$' + c.reset + ' '
  while True:
    try:
      command = input(cursor)
      if command == '<>end15<>':
        print('Fine...')
        break
      command = command.split(' ')
      command = command.pop(0)
      command = re.sub('\\W*','',command)
      if command == '':
        continue
      time.sleep(.2)
      print(command + ': command not found')
    except (KeyboardInterrupt,EOFError,RuntimeError):
      print()

trolling('error404','skilstak','side-projects')
