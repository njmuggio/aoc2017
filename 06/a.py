#!/usr/bin/env python3

import sys

class Bank:
  def __init__(self, id, blocks) -> None:
    self.id = id
    self.blocks = blocks
  id: int
  blocks: int

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  banks = []
  for idx, num in enumerate([int(x) for x in f.readline().split()]):
    banks.append(Bank(idx, num))

history = set()
history.add(tuple(b.blocks for b in sorted(banks, key=lambda b: b.id)))

while True:
  banks.sort(key=lambda b: b.id, reverse=True)
  banks.sort(key=lambda b: b.blocks)
  id = banks[-1].id
  blocks = banks[-1].blocks
  banks[-1].blocks = 0
  banks.sort(key=lambda b: b.id)

  for n in range(blocks):
    id = (id + 1) % len(banks)
    banks[id].blocks += 1

  before = len(history)
  # print(tuple(b.blocks for b in sorted(banks, key=lambda b: b.id)))
  history.add(tuple(b.blocks for b in sorted(banks, key=lambda b: b.id)))
  after = len(history)
  if before == after:
    break

print(len(history))
