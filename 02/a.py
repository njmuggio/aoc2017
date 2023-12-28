#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  total = 0
  for line in f:
    nums = [int(chunk) for chunk in line.split(None)]
    nums = sorted(nums)
    total += nums[-1] - nums[0]
print(total)
