#!/usr/bin/env python3

import sys

def getDist(_noso, _nwse):
  totalDist = abs(_noso + _nwse)
  if _noso > 0 and _nwse > 0:
    totalDist -= min(_noso, _nwse)
  if _noso < 0 and _nwse < 0:
    totalDist -= min(abs(_noso), abs(_nwse))
  return totalDist

maxTotalDist = 0
noso = 0
nwse = 0
with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for d in f.readline().strip().split(","):
    match d:
      case "n":
        noso += 1
      case "ne":
        noso += 1
        nwse += 1
      case "se":
        nwse += 1
      case "s":
        noso -= 1
      case "sw":
        noso -= 1
        nwse -= 1
      case "nw":
        nwse -= 1
    maxTotalDist = max(maxTotalDist, getDist(noso, nwse))

print(maxTotalDist)
