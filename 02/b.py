#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  total = 0
  for line in f:
    nums = [int(chunk) for chunk in line.split(None)]
    for a in nums:
      for b in nums:
        if a == b:
          continue
        if a / b == a // b:
          total += a // b
          break
print(total)
