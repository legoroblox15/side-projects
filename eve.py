#!/usr/bin/env python3
import skilstak.colors as c
import time
import random
'''
Eve's brain is set up in an interesting way. Since Eve needs to do different things based on the temperature of the previous guess, she needs to have
two sperate sub-lists
'''
strat_stats = {}
strats = []

for strat in range(1000):
  strats.append([])


def clear():
  print(c.clear,end='')
  
def run_strat(strat,printing=False):
  