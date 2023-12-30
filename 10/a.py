#!/usr/bin/env python3

import sys

nums = []
for i in range(0, 256):
  nums.append(i)

idx = 0

def get(i):
  return nums[i % len(nums)]

def set(i, v):
  nums[i % len(nums)] = v

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for skip, length in enumerate([int(x) for x in f.readline().split(",")]):
    revList = []
    for i in range(length):
      revList.append(get(idx + i))
    revList.reverse()
    for i in range(length):
      set(idx + i, revList[i])
    idx += length + skip

print(nums[0] * nums[1])
