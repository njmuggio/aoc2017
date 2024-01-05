#!/usr/bin/env python3

import sys

class Edge:
  def __init__(self, a, b) -> None:
    self.a = int(a)
    self.b = int(b)
    self.neighbors = set()

  def __hash__(self) -> int:
    return id(self)

  def __str__(self):
    return f"{self.a}/{self.b}"

  def getNeighbors(self, inbound):
    if self.a == self.b:
      return self.neighbors.difference({inbound})
    elif self.a == inbound.a or self.a == inbound.b:
      return set(n for n in self.neighbors if self.b == n.a or self.b == n.b)
    elif self.b == inbound.a or self.b == inbound.b:
      return set(n for n in self.neighbors if self.a == n.a or self.a == n.b)
    assert False

edges = [Edge(0, 0)]

edgesByVal = {0: {edges[0]}}

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    a, b = line.strip().split("/")
    edge = Edge(a, b)
    edges.append(edge)

    if edge.a not in edgesByVal:
      edgesByVal[edge.a] = {edge}
    else:
      edgesByVal[edge.a].add(edge)

    if edge.b not in edgesByVal:
      edgesByVal[edge.b] = {edge}
    else:
      edgesByVal[edge.b].add(edge)

for edgeSet in edgesByVal.values():
  for edge in edgeSet:
    edge.neighbors.update(edgeSet)
    edge.neighbors.remove(edge)

maxDist = 0

def explore(edge: Edge, history: list[Edge]) -> int:
  global maxDist

  neighbors = edge.getNeighbors(history[-1] if history else Edge(-1, -1))
  history.append(edge)

  for neighbor in neighbors.difference(history):
    explore(neighbor, history)

  totalStrength = sum(h.a + h.b for h in history)
  maxDist = max(maxDist, totalStrength)

  history.pop()

explore(edges[0], [])

print(maxDist)
