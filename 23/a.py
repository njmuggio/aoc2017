#!/usr/bin/env python3

import sys

reg = {}

def iors(a):
  try:
    return int(a)
  except:
    return a

class Opcode:
  pass

Opcode.SET = 0
Opcode.SUB = 1
Opcode.MUL = 2
Opcode.JNZ = 3

class Inst:
  def __init__(self, op, a, b) -> None:
    self.op = op
    self.a = iors(a)
    self.b = iors(b)

class Reg:
  def __init__(self) -> None:
    self.d = {}

  def __getitem__(self, name):
    if isinstance(name, int):
      return name

    if name not in self.d:
      self.d[name] = 0

    return self.d[name]

  def __setitem__(self, name, val):
    self.d[name] = val

prog = []

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    mne, a, b = line.split()
    match mne:
      case "set":
        op = Opcode.SET
      case "sub":
        op = Opcode.SUB
      case "mul":
        op = Opcode.MUL
      case "jnz":
        op = Opcode.JNZ
    prog.append(Inst(op, a, b))

reg = Reg()
pc = 0
mulCount = 0

while 0 <= pc < len(prog):
  inst = prog[pc]
  pc += 1
  match inst.op:
    case Opcode.SET:
      reg[inst.a] = reg[inst.b]
    case Opcode.SUB:
      reg[inst.a] -= reg[inst.b]
    case Opcode.MUL:
      reg[inst.a] *= reg[inst.b]
      mulCount += 1
    case Opcode.JNZ:
      if reg[inst.a] != 0:
        pc += reg[inst.b] - 1

print(mulCount)
