#!/usr/bin/env python3

import sys

lines = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    lines.append(line.removesuffix("\n"))

x = lines[0].find("|")
y = 0
dx = 0
dy = 1

def get(x, y):
  if 0 <= y < len(lines):
    if 0 <= x < len(lines[y]):
      return lines[y][x]
  return " "

letters = ""
steps = 0

while True:
  steps += 1
  nx = x + dx
  ny = y + dy
  next = get(nx, ny)
  if ord("A") <= ord(next) <= ord("Z"):
    letters += next
  elif next == "+":
    if abs(dy):
      left = get(x - 1, y + dy)
      right = get(x + 1, y + dy)
      if left != " ":
        dx = -1
        dy = 0
      elif right != " ":
        dx = 1
        dy = 0
      else:
        assert False
    elif abs(dx):
      up = get(x + dx, y - 1)
      down = get(x + dx, y + 1)
      if up != " ":
        dx = 0
        dy = -1
      elif down != " ":
        dx = 0
        dy = 1
      else:
        assert False
    else:
      assert False
  elif next == " ":
    break

  x = nx
  y = ny

print(steps)
