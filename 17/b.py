#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  step = int(f.readline().strip())


bufLen = 1
idx = 0
lastIdx1 = -1

for bufLen in range(1, 50000001):
  idx += step
  idx %= bufLen
  if idx == 0:
    lastIdx1 = bufLen
  idx += 1

print(lastIdx1)
