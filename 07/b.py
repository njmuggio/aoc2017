#!/usr/bin/env python3

import sys

class Wobbleprog:
  def __init__(self, name: str, weight: int, childNames: list[str]):
    self.name = name
    self.weight = weight
    self.childNames = childNames
    self.children = []
    self.parent = None
    self.totalWeight = 0
    self.balanced = True


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

def fillTotalWeight(node: Wobbleprog):
  node.totalWeight = node.weight
  for child in node.children:
    node.totalWeight += fillTotalWeight(child)
  node.children.sort(key=lambda c: c.totalWeight)
  if len(node.children) > 1:
    if node.children[0].totalWeight != node.children[1].totalWeight:
      print(node.children[1].totalWeight - node.children[0].totalWeight + node.children[0].weight)
      exit(0)
    elif node.children[-1].totalWeight != node.children[-2].totalWeight:
      print(node.children[-1].weight - (node.children[-1].totalWeight - node.children[-2].totalWeight))
      exit(0)
  return node.totalWeight

roots = [prog for prog in progs.values() if prog.parent is None]
fillTotalWeight(roots[0])
