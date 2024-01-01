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

    self.collision = False

  def __eq__(self, __value: object) -> bool:
    return self.x == __value.x and self.y == __value.y and self.z == __value.z

  def __str__(self) -> str:
    return f"{self.num}:\t<{self.x},{self.y},{self.z}>"

points = []

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for num, line in enumerate(f):
    pvaChunks = line.strip().split(", ")
    pos = [int(p) for p in pvaChunks[0].removeprefix("p=<").removesuffix(">").split(",")]
    vel = [int(v) for v in pvaChunks[1].removeprefix("v=<").removesuffix(">").split(",")]
    acc = [int(a) for a in pvaChunks[2].removeprefix("a=<").removesuffix(">").split(",")]
    points.append(Point(num, pos[0], pos[1], pos[2], vel[0], vel[1], vel[2], acc[0], acc[1], acc[2]))

def collisionsPossible():
  return len(points) > 1

escaped = []

step = 0
while collisionsPossible():
  step += 1
  mins = Point(-1, points[0].x, points[0].y, points[0].z, points[0].vx, points[0].vy, points[0].vz, points[0].ax, points[0].ay, points[0].az)
  maxes = Point(-1, points[0].x, points[0].y, points[0].z, points[0].vx, points[0].vy, points[0].vz, points[0].ax, points[0].ay, points[0].az)

  for p in points:
    p.vx += p.ax
    p.vy += p.ay
    p.vz += p.az
    p.x += p.vx
    p.y += p.vy
    p.z += p.vz

    mins.x = min(mins.x, p.x)
    mins.y = min(mins.y, p.y)
    mins.z = min(mins.z, p.z)
    mins.vx = min(mins.vx, p.vx)
    mins.vy = min(mins.vy, p.vy)
    mins.vz = min(mins.vz, p.vz)
    mins.ax = min(mins.ax, p.ax)
    mins.ay = min(mins.ay, p.ay)
    mins.az = min(mins.az, p.az)

    maxes.x = max(maxes.x, p.x)
    maxes.y = max(maxes.y, p.y)
    maxes.z = max(maxes.z, p.z)
    maxes.vx = max(maxes.vx, p.vx)
    maxes.vy = max(maxes.vy, p.vy)
    maxes.vz = max(maxes.vz, p.vz)
    maxes.ax = max(maxes.ax, p.ax)
    maxes.ay = max(maxes.ay, p.ay)
    maxes.az = max(maxes.az, p.az)

  collision = False
  for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
      if points[i] == points[j]:
        collision = True
        points[i].collision = True
        points[j].collision = True

  points = [p for p in points if not p.collision]

  for p in points:
    if p.x == mins.x and p.vx == mins.vx and p.ax == mins.ax:
      p.collision = True
    elif p.y == mins.y and p.vy == mins.vy and p.ay == mins.ay:
      p.collision = True
    elif p.z == mins.z and p.vz == mins.vz and p.az == mins.az:
      p.collision = True
    elif p.x == maxes.x and p.vx == maxes.vx and p.ax == maxes.ax:
      p.collision = True
    elif p.y == maxes.y and p.vy == maxes.vy and p.ay == maxes.ay:
      p.collision = True
    elif p.z == maxes.z and p.vz == maxes.vz and p.az == maxes.az:
      p.collision = True

  escaped += [p for p in points if p.collision]
  points = [p for p in points if not p.collision]

print(len(points) + len(escaped))
