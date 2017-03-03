#!/usr/bin/env python3
import skilstak.colors as c
def clear():
  print(c.clear + c.reset,end='')

def ask(prompt,answer_type=str,answer_line='>>> ',allow=[],veto=[],use_getch=False):

    # Function Description:  Function that acts as a smart input statement that only allows input of certain data types. Also whitelists and blacklists specific inputs.

    # Variable decriptions:
    # - prompt: Prints the message like a normal input statement.
    # - answer_type: The desired data type that you want the user to input.
    # - answer_line: Text before line feed.
    # - allow: whitelists specific inputs.
    # - veto: blacklists specific learning.
    # - use_getch: takes input from a single keystroke 

  answer = None
  if use_getch and answer_type not in [list, dict]:
    import getch
  else:
    use_getch = False
  
  if answer_type in (list, dict):
    from ast import literal_eval

  while answer in veto or not isinstance(answer, answer_type) or answer not in allow and allow != []: # If answer is one of the vetoed words, if it couldn't cast into the wanted type, or answer is not one of the allowed words (only if there is atleast one allowed word), then continue running the loop.
    clear()
    
    print(prompt + '\n' + answer_line,end='')
    try:
      answer = getch.getch()
    except UnboundLocalError:
      answer = input()

    try:
      if answer_type == int:
        answer = int(answer)
      elif answer_type == float:
        answer = float(answer)
      elif answer_type in (list, dict):
        answer = literal_eval(answer)
    
    except (ValueError, SyntaxError):
      pass
  clear()

  return answer

if __name__ == '__main__':
  ask('Give me an Int!',int)
  ask('Give me an Float!',float)
  ask('Give me a String!')
  ask('Give me a List!',list)
  ask('Give me a Dictionary!',dict)
