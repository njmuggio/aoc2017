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

disk = []
for i in range(128):
  disk.append([0] * 128)

for i in range(128):
  h = knotHash(f"{seed}-{i}")
  for b in range(128):
    if h & (1 << b):
      disk[i][b] = 1

def eraseRegion(startX, startY):
  field = [(startX, startY)]
  while field:
    point = field.pop()
    disk[point[1]][point[0]] = 0
    if point[0] > 0 and disk[point[1]][point[0] - 1]:
      field.append((point[0] - 1, point[1]))
    if point[0] < 127 and disk[point[1]][point[0] + 1]:
      field.append((point[0] + 1, point[1]))
    if point[1] > 0 and disk[point[1] - 1][point[0]]:
      field.append((point[0], point[1] - 1))
    if point[1] < 127 and disk[point[1] + 1][point[0]]:
      field.append((point[0], point[1] + 1))

regionCount = 0
for y in range(128):
  for x in range(128):
    if disk[y][x]:
      eraseRegion(x, y)
      regionCount += 1

print(regionCount)
