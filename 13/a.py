#!/usr/bin/env python3

import sys

class Scanner:
  def __init__(self, layer, depth) -> None:
    self.layer = layer
    self.location = 0
    self.depth = depth
    self.direction = 1
    self.severity = layer * depth

  def advance(self):
    if (self.direction == 1 and self.location == self.depth - 1) or (self.direction == -1 and self.location == 0):
      self.direction *= -1
    self.location += self.direction

scanners = {}
maxLayer = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    layer, depth = line.split(": ")
    layer = int(layer)
    depth = int(depth)
    scanners[layer] = Scanner(layer, depth)
    maxLayer = max(maxLayer, layer)

curLayer = -1
severity = 0
for i in range(maxLayer + 1):
  curLayer += 1
  if curLayer in scanners and scanners[curLayer].location == 0:
    severity += scanners[curLayer].severity
  for scanner in scanners.values():
    scanner.advance()

print(severity)
