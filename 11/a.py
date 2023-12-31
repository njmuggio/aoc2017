#!/usr/bin/env python3

import sys

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

totalDist = abs(noso + nwse)
if noso > 0 and nwse > 0:
  totalDist -= min(noso, nwse)
if noso < 0 and nwse < 0:
  totalDist -= min(abs(noso), abs(nwse))
print(totalDist)
