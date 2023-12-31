#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  parts = f.readline().split()
  a = int(parts[0])
  b = int(parts[1])

matches = 0
for i in range(40000000):
  a = (a * 16807) % 2147483647
  b = (b * 48271) % 2147483647
  if (a & 0xFFFF) == (b & 0xFFFF):
    matches += 1

print(matches)
