#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  jumps = []
  for line in f:
    jumps.append(int(line))

idx = 0
steps = 0
while 0 <= idx < len(jumps):
  steps += 1
  next = jumps[idx]
  jumps[idx] += -1 if jumps[idx] >= 3 else 1
  idx += next
print(steps)
