#!/usr/bin/env python3

import sys

prog = []
reg = {}
pc = 0
lastSnd = 0
rcvCount = 0
lastRcv = 0

def get(r):
  if isinstance(r, int):
    return r

  if r not in reg:
    reg[r] = 0
  return reg[r]

def set(r, v):
  reg[r] = v

class Snd:
  def __init__(self, r) -> None:
    self.r = r

  def run(self):
    global lastSnd
    lastSnd = get(self.r)

class Set:
  def __init__(self, r, v) -> None:
    self.r = r
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self):
    set(self.r, get(self.v))

class Add:
  def __init__(self, r, v) -> None:
    self.r = r
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self):
    set(self.r, get(self.r) + get(self.v))

class Mul:
  def __init__(self, r, v) -> None:
    self.r = r
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self):
    set(self.r, get(self.r) * get(self.v))

class Mod:
  def __init__(self, r, v) -> None:
    self.r = r
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self):
    set(self.r, get(self.r) % get(self.v))

class Rcv:
  def __init__(self, r) -> None:
    self.r = r

  def run(self):
    global lastRcv
    global lastSnd
    global rcvCount
    if get(self.r):
      lastRcv = lastSnd
      rcvCount += 1

class Jgz:
  def __init__(self, r, v) -> None:
    self.r = r
    try:
      self.v = int(v)
    except:
      self.v = v

  def run(self):
    global pc
    if get(self.r) > 0:
      pc += get(self.v)
      pc -= 1

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    parts = line.split()
    match parts[0]:
      case "snd":
        prog.append(Snd(parts[1]))
      case "set":
        prog.append(Set(parts[1], parts[2]))
      case "add":
        prog.append(Add(parts[1], parts[2]))
      case "mul":
        prog.append(Mul(parts[1], parts[2]))
      case "mod":
        prog.append(Mod(parts[1], parts[2]))
      case "rcv":
        prog.append(Rcv(parts[1]))
      case "jgz":
        prog.append(Jgz(parts[1], parts[2]))

while rcvCount == 0:
  assert 0 <= pc < len(prog)
  prog[pc].run()
  pc += 1

print(lastRcv)
