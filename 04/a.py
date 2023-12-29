#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  valid = 0
  for line in f:
    words = sorted(line.split())
    setWords = set(words)
    if len(words) == len(setWords):
      valid += 1
print(valid)
