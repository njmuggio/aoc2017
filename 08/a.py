#!/usr/bin/env python3

import sys

reg = {}

def get(name):
  if name not in reg:
    reg[name] = 0
  return reg[name]

def inc(name, val):
  get(name)
  reg[name] += val

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    name, mod, val, _, dep, cond, comp = line.split()

    val = int(val)
    comp = int(comp)

    if mod == "dec":
      val = -val

    if cond == ">" and get(dep) > comp:
      inc(name, val)
    elif cond == "<" and get(dep) < comp:
      inc(name, val)
    elif cond == ">=" and get(dep) >= comp:
      inc(name, val)
    elif cond == "<=" and get(dep) <= comp:
      inc(name, val)
    elif cond == "!=" and get(dep) != comp:
      inc(name, val)
    elif cond == "==" and get(dep) == comp:
      inc(name, val)

vals = sorted(reg.values())
print(vals[-1])
