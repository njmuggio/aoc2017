#!/usr/bin/env python3

import sys

class Scanner:
  def __init__(self, layer, depth) -> None:
    self.layer = layer
    self.depth = depth

    self.cycleTime = self.depth * 2 - 2

  def isZero(self, time):
    return time % self.cycleTime == 0

scanners = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    layer, depth = line.split(": ")
    layer = int(layer)
    depth = int(depth)
    scanners.append(Scanner(layer, depth))


def test(delay):
  for s in scanners:
    if s.isZero(delay + s.layer):
      return True
  return False

caught = True
delay = -1
while caught:
  delay += 1
  caught = test(delay)

print(delay)
