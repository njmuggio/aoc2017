#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  targetAddr = int(f.readline())

oddSqRt = 1
while (oddSqRt ** 2) < targetAddr:
  oddSqRt += 2
corner = oddSqRt ** 2

off = (oddSqRt - 1)
centers = [corner - off // 2]
centers.append(centers[0] - off)
centers.append(centers[1] - off)
centers.append(centers[2] - off)

diffs = [abs(targetAddr - center) for center in centers]
print(min(diffs) + oddSqRt // 2)
