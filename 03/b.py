#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  targetVal = int(f.readline())

spiral = {0: {0: 1}}
fillSize = 0

def get(x, y):
  if x not in spiral:
    # print("  get", x, y)
    return 0
  if y not in spiral[x]:
    # print("  get", x, y)
    return 0
  # print("  get", x, y, "->", spiral[x][y])
  return spiral[x][y]

def add(x, y):
  # print("add", x, y)
  if x not in spiral:
    spiral[x] = {}
  total = 0
  for ox in range(x - 1, x + 2):
    for oy in range(y - 1, y + 2):
      total += get(ox, oy)
  spiral[x][y] = total
  if total > targetVal:
    print(total)
    exit(0)

curX = 0
curY = 0
while True:
  fillSize += 2
  curX += 1
  for n in range(fillSize):
    add(curX, curY)
    curY -= 1
  curY += 1
  curX -= 1
  for n in range(fillSize):
    add(curX, curY)
    curX -= 1
  curX += 1
  curY += 1
  for n in range(fillSize):
    add(curX, curY)
    curY += 1
  curY -= 1
  curX += 1
  for n in range(fillSize):
    add(curX, curY)
    curX += 1
  curX -= 1
