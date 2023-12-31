#!/usr/bin/env python3

import sys

def knotHash(s):
  nums = list(range(256))

  idx = 0
  skip = 0

  def get(i):
    return nums[i % len(nums)]

  def set(i, v):
    nums[i % len(nums)] = v

  lengths = []

  for c in s:
    lengths.append(ord(c))

  lengths += [17, 31, 73, 47, 23]

  for _ in range(64):
    for length in lengths:
      revList = []
      for i in range(length):
        revList.append(get(idx + i))
      revList.reverse()
      for i in range(length):
        set(idx + i, revList[i])
      idx += length + skip
      skip += 1

  final = 0
  dense = []
  for i in range(16):
    val = 0
    for j in range(16):
      val ^= nums[i * 16 + j]
    final = (final << 8) | val

  return final

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  seed = f.readline().strip()

used = 0
for i in range(128):
  h = knotHash(f"{seed}-{i}")
  while h:
    if h & 0x01:
      used += 1
    h >>= 1

print(used)
