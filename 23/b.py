#!/usr/bin/env python3

import sys
import subprocess

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

  def __str__(self):
    match self.op:
      case Opcode.SET:
        r = "set "
      case Opcode.SUB:
        r = "sub "
      case Opcode.MUL:
        r = "mul "
      case Opcode.JNZ:
        r = "jnz "
    r += a + " " + b
    return r

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

  def __str__(self):
    return str(self.d)

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

with open("/tmp/aoc23-2.c", mode="wt", encoding="utf-8") as source:
  source.write("""
#include <stdio.h>
int main() {
  int a = 1, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0;
""")

  for i, inst in enumerate(prog):
    source.write(f"inst_{i}:\n")
    source.write(f"  // {str(inst)}\n")
    match inst.op:
      case Opcode.SET:
        source.write(f"  {inst.a} = {inst.b};\n")
      case Opcode.SUB:
        source.write(f"  {inst.a} -= {inst.b};\n")
      case Opcode.MUL:
        source.write(f"  {inst.a} *= {inst.b};\n")
      case Opcode.JNZ:
        source.write(f"  if ({inst.a} != 0) goto inst_{i + inst.b};\n")

  source.write(f"""
inst_{i + 1}:
  printf("%d\\n", h);
}}
""")

subprocess.run(["gcc", "-std=c99", "-Ofast", "-march=native", "-o", "/tmp/aoc23-2", "/tmp/aoc23-2.c"], check=True)
subprocess.run(["/tmp/aoc23-2"])
