#!/usr/bin/env python3

import sys

class Node:
  def __init__(self, id, remoteIds) -> None:
    self.id = id
    self.remoteIds = remoteIds
    self.visited = False

nodes = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    parts = line.split()
    id = parts[0]
    remoteIds = [int(x.removesuffix(",")) for x in parts[2:]]
    nodes.append(Node(id, remoteIds))

count = 0
field = [nodes[0]]
while len(field) > 0:
  cur = field.pop()
  if cur.visited:
    continue
  cur.visited = True
  field += [nodes[remote] for remote in cur.remoteIds if not nodes[remote].visited]
  count += 1

print(count)
