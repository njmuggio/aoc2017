#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  line = f.readline().strip()
  total = 0
  line2 = line[1:] + line[0]
  for i in range(len(line)):
    if line[i] == line2[i]:
      total += ord(line[i]) - ord('0')
print(total)
