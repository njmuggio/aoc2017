#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  stream = f.readline().strip()

canceled = stream.find("!")
while canceled >= 0:
  stream = stream[:canceled] + stream[canceled + 2:]
  canceled = stream.find("!")

garbageStart = stream.find("<")
while garbageStart >= 0:
  garbageEnd = stream.find(">")
  stream = stream[:garbageStart] + stream[garbageEnd + 1:]
  garbageStart = stream.find("<")

totalScore = 0

level = 0
for c in stream:
  if c == '{':
    level += 1
    totalScore += level
  elif c == '}':
    level -= 1

print(totalScore)
