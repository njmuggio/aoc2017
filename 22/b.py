#!/usr/bin/env python3

import sys

class State:
  pass

State.CLEAN = 0
State.WEAKENED = 1
State.INFECTED = 2
State.FLAGGED = 3

class Cells:
  def __init__(self) -> None:
    self.cells = {}

  def __getitem__(self, coords):
    if coords in self.cells:
      return self.cells[coords]
    return State.CLEAN

  def __setitem__(self, coords, value):
    if value == State.CLEAN:
      if coords in self.cells:
        del self.cells[coords]
    else:
      self.cells[coords] = value

cells = Cells()
carrier = (0, 0)

facing = (0, -1)

def right(f):
  return (f[1] * -1, f[0])

def left(f):
  return (f[1], f[0] * -1)

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for y, line in enumerate(f):
    line = line.strip()
    for x, c in enumerate(line):
      if c == "#":
        cells[x, y] = State.INFECTED

  carrier = (x // 2, y // 2)

infections = 0

for step in range(10000000):
  match cells[carrier]:
    case State.CLEAN:
      facing = left(facing)
      cells[carrier] = State.WEAKENED
    case State.WEAKENED:
      cells[carrier] = State.INFECTED
      infections += 1
    case State.INFECTED:
      facing = right(facing)
      cells[carrier] = State.FLAGGED
    case State.FLAGGED:
      facing = right(right(facing))
      cells[carrier] = State.CLEAN

  carrier = (carrier[0] + facing[0], carrier[1] + facing[1])

print(infections)
