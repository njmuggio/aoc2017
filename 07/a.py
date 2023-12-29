#!/usr/bin/env python3

import sys

class Wobbleprog:
  def __init__(self, name: str, weight: int, childNames: list[str]):
    self.name = name
    self.weight = weight
    self.childNames = childNames
    self.children = []
    self.parent = None


with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  progs = {}
  for line in f:
    parts = line.split()
    name = parts[0]
    weight = int(parts[1][1:-1])
    childNames = [n.removesuffix(",") for n in parts[3:]]
    progs[name] = Wobbleprog(name, weight, childNames)

for name, prog in progs.items():
  for childName in prog.childNames:
    prog.children.append(progs[childName])
    progs[childName].parent = prog

roots = [prog for prog in progs.values() if prog.parent is None]
print(roots[0].name)
