#!/usr/bin/env python3

import sys

class Machine:
  def __init__(self, id) -> None:
    self.id = id
    self.prog = []
    self.reg = {}
    self.reg["p"] = id
    self.pc = 0
    self.sendQueue = []
    self.recvFrom = None
    self.sendCount = 0

  def __str__(self) -> str:
    return f"M:{self.id} PC:{self.pc} SQ:{len(self.sendQueue)} SC:{self.sendCount} R:{self.reg}"

  def get(self, r):
    if isinstance(r, int):
      return r

    if r not in self.reg:
      self.reg[r] = 0
    return self.reg[r]

  def set(self, r, v):
    self.reg[r] = v

  def send(self, v):
    assert isinstance(v, int)
    self.sendQueue.append(v)
    self.sendCount += 1

  def recv(self) -> tuple[bool, int | None]:
    assert self.recvFrom

    if not self.recvFrom.sendQueue:
      return (False, None)
    val = self.recvFrom.sendQueue.pop(0)
    return (True, val)

  def step(self):
    if self.pc < 0 or self.pc >= len(self.prog):
      return False

    pcBefore = self.pc
    self.prog[self.pc].run(self)
    self.pc += 1
    return pcBefore != self.pc

class Snd:
  def __init__(self, v) -> None:
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self, m):
    m.send(m.get(self.v))

class Set:
  def __init__(self, r, v) -> None:
    self.r = r
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self, m):
    m.set(self.r, m.get(self.v))

class Add:
  def __init__(self, r, v) -> None:
    self.r = r
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self, m):
    m.set(self.r, m.get(self.r) + m.get(self.v))

class Mul:
  def __init__(self, r, v) -> None:
    self.r = r
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self, m):
    m.set(self.r, m.get(self.r) * m.get(self.v))

class Mod:
  def __init__(self, r, v) -> None:
    self.r = r
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self, m):
    m.set(self.r, m.get(self.r) % m.get(self.v))

class Rcv:
  def __init__(self, r) -> None:
    self.r = r

  def run(self, m):
    received, val = m.recv()
    if received:
      m.set(self.r, val)
    else:
      m.pc -= 1

class Jgz:
  def __init__(self, r, v) -> None:
    try:
      self.r = int(r)
    except:
      self.r = r

    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self, m):
    if m.get(self.r) > 0:
      m.pc += m.get(self.v)
      m.pc -= 1

m0 = Machine(0)
m1 = Machine(1)

m0.recvFrom = m1
m1.recvFrom = m0

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    parts = line.split()
    match parts[0]:
      case "snd":
        m0.prog.append(Snd(parts[1]))
        m1.prog.append(Snd(parts[1]))
      case "set":
        m0.prog.append(Set(parts[1], parts[2]))
        m1.prog.append(Set(parts[1], parts[2]))
      case "add":
        m0.prog.append(Add(parts[1], parts[2]))
        m1.prog.append(Add(parts[1], parts[2]))
      case "mul":
        m0.prog.append(Mul(parts[1], parts[2]))
        m1.prog.append(Mul(parts[1], parts[2]))
      case "mod":
        m0.prog.append(Mod(parts[1], parts[2]))
        m1.prog.append(Mod(parts[1], parts[2]))
      case "rcv":
        m0.prog.append(Rcv(parts[1]))
        m1.prog.append(Rcv(parts[1]))
      case "jgz":
        m0.prog.append(Jgz(parts[1], parts[2]))
        m1.prog.append(Jgz(parts[1], parts[2]))

m0Advanced = True
m1Advanced = True
step = 0
while m0Advanced or m1Advanced:
  m0Advanced = m0.step()
  m1Advanced = m1.step()

print(m1.sendCount)
