#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  step = int(f.readline().strip())

buf = [0]
idx = 0

for i in range(1, 2018):
  idx += step
  idx %= len(buf)
  buf.insert(idx + 1, i)
  idx += 1

idx = buf.index(2017)
print(buf[idx + 1])
