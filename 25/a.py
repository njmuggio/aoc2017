#!/usr/bin/env python3

import sys

class State:
  def __init__(self, vals, dirs, transitions):
    self.vals = vals
    self.dirs = dirs
    self.transitions = transitions

states = {}

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  line = f.readline().split()
  curState = line[-1][0]

  line = f.readline().split()
  steps = int(line[5])

  while True:
    try:
      vals = [0, 0]
      dirs = [0, 0]
      transitions = ["", ""]

      f.readline()
      stateName = f.readline().split()[-1][0]
      f.readline()
      vals[0] = int(f.readline().split()[-1][0])
      dirs[0] = 1 if f.readline().split()[-1] == "right." else -1
      transitions[0] = f.readline().split()[-1][0]
      f.readline()
      vals[1] = int(f.readline().split()[-1][0])
      dirs[1] = 1 if f.readline().split()[-1] == "right." else -1
      transitions[1] = f.readline().split()[-1][0]

      states[stateName] = State(vals, dirs, transitions)
    except:
      break

tape = [0]
head = 0

def get():
  global head
  if head == -1:
    tape.insert(0, 0)
    head += 1
  elif head == len(tape):
    tape.append(0)

  return tape[head]

while steps > 0:
  steps -= 1
  val = get()
  tape[head] = states[curState].vals[val]
  head += states[curState].dirs[val]
  curState = states[curState].transitions[val]

print(sum(tape))
