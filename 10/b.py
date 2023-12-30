#!/usr/bin/env python3

import sys

nums = []
for i in range(0, 256):
  nums.append(i)

idx = 0
skip = 0

def get(i):
  return nums[i % len(nums)]

def set(i, v):
  nums[i % len(nums)] = v

lengths = []

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for c in f.readline().strip():
    lengths.append(ord(c))

lengths += [17, 31, 73, 47, 23]

for round in range(64):
  for length in lengths:
    revList = []
    for i in range(length):
      revList.append(get(idx + i))
    revList.reverse()
    for i in range(length):
      set(idx + i, revList[i])
    idx += length + skip
    skip += 1

dense = []
for i in range(16):
  val = 0
  for j in range(16):
    val ^= nums[i * 16 + j]
  dense.append(val)

final = 0
for b in dense:
  final = final << 8
  final |= b

print(hex(final)[2:])
