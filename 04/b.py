#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  valid = 0
  for line in f:
    words = sorted(line.split())
    newWords = []
    for word in words:
      newWords.append(''.join(sorted(c for c in word)))
    setWords = set(newWords)
    if len(setWords) == len(newWords):
      valid += 1
print(valid)
