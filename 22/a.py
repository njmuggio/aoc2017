#!/usr/bin/env python3

import sys

class Cells:
  def __init__(self) -> None:
    self.cells = set()

  def __getitem__(self, coords):
    return coords in self.cells

  def __setitem__(self, coords, value):
    if value:
      self.cells.add(coords)
    elif coords in self.cells:
      self.cells.remove(coords)

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
        cells[x, y] = True

  carrier = (x // 2, y // 2)

infections = 0

for step in range(10000):
  if cells[carrier]:
    facing = right(facing)
    cells[carrier] = False
  else:
    facing = left(facing)
    cells[carrier] = True
    infections += 1

  carrier = (carrier[0] + facing[0], carrier[1] + facing[1])

print(infections)
