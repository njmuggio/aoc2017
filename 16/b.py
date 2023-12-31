#!/usr/bin/env python3

import sys

class Inst:
  def __init__(self) -> None:
    pass

  def run(self, l: list[str]) -> None:
    pass

class Spin(Inst):
  def __init__(self, num) -> None:
    super().__init__()
    self.num = num

  def run(self, l: list[str]) -> None:
    for _ in range(self.num):
      l.insert(0, l.pop())

class Exchange(Inst):
  def __init__(self, idxA: int, idxB: int) -> None:
    super().__init__()
    self.idxA: int = idxA
    self.idxB: int = idxB

  def run(self, l: list[str]) -> None:
    t = l[self.idxA]
    l[self.idxA] = l[self.idxB]
    l[self.idxB] = t

class Partner(Inst):
  def __init__(self, charA: str, charB: str) -> None:
    super().__init__()
    self.charA: str = charA
    self.charB: str = charB

  def run(self, l: list[str]) -> None:
    idxA: int = l.index(self.charA)
    idxB: int = l.index(self.charB)

    t = l[idxA]
    l[idxA] = l[idxB]
    l[idxB] = t

prog = []
with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for inst in (f.readline().strip().split(",")):
    if inst[0] == "s":
      prog.append(Spin(int(inst[1:])))
    elif inst[0] == "x":
      nums = inst[1:].split("/")
      prog.append(Exchange(int(nums[0]), int(nums[1])))
    elif inst[0] == "p":
      prog.append(Partner(inst[1], inst[3]))

line = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
i = 0
while i == 0 or ''.join(line) != "abcdefghijklmnop":
  for inst in prog:
    inst.run(line)
  i += 1
i = (1000000000 - (1000000000 % i))

while i < 1000000000:
  for inst in prog:
    inst.run(line)
  i += 1

print(''.join(line))
