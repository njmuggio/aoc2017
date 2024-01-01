#!/usr/bin/env python3

import sys

class Point:
  def __init__(self, num, x, y, z, vx, vy, vz, ax, ay, az) -> None:
    self.num = num

    self.x = x
    self.y = y
    self.z = z
    self.vx = vx
    self.vy = vy
    self.vz = vz
    self.ax = ax
    self.ay = ay
    self.az = az

    self.x2 = 0
    self.y2 = 0
    self.z2 = 0

points = []

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for num, line in enumerate(f):
    pvaChunks = line.strip().split(", ")
    pos = [int(p) for p in pvaChunks[0].removeprefix("p=<").removesuffix(">").split(",")]
    vel = [int(v) for v in pvaChunks[1].removeprefix("v=<").removesuffix(">").split(",")]
    acc = [int(a) for a in pvaChunks[2].removeprefix("a=<").removesuffix(">").split(",")]
    points.append(Point(num, pos[0], pos[1], pos[2], vel[0], vel[1], vel[2], acc[0], acc[1], acc[2]))

t = 100000000000000000000000000000000
for p in points:
  p.x2 = p.x + p.vx * t - p.ax * (t ** 2) / 2
  p.y2 = p.y + p.vy * t - p.ay * (t ** 2) / 2
  p.z2 = p.z + p.vz * t - p.az * (t ** 2) / 2

points.sort(key=lambda p: abs(p.x2) + abs(p.y2) + abs(p.z2))
print(points[0].num)
