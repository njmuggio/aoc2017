#!/usr/bin/env python3

import sys

size = 3
image = [0b010, 0b001, 0b111]

replaceTwo = {}
# for start in range(0b1_00_00):
#   replaceTwo[start] = 0

replaceThree = {}
# for start in range(0b1_000_000_000):
#   replaceThree[start] = 0

def move(n, start, end):
  n = n & (1 << start)
  n >>= start
  return n << end

def flipHoriz2(n):
  """
  32
  10

  3 -> 2
  2 -> 3
  1 -> 0
  0 -> 1
  """
  r = move(n, 3, 2)
  r |= move(n, 2, 3)
  r |= move(n, 1, 0)
  r |= move(n, 0, 1)
  return r

def rotateRight2(n):
  """
  32
  10

  3 -> 2
  2 -> 0
  0 -> 1
  1 -> 3
  """
  r = move(n, 3, 2)
  r |= move(n, 2, 0)
  r |= move(n, 0, 1)
  r |= move(n, 1, 3)
  return r

def flipHoriz3(n):
  """
  876
  543
  210

  8 -> 6
  7 -> 7
  6 -> 8
  5 -> 3
  4 -> 4
  3 -> 5
  2 -> 0
  1 -> 1
  0 -> 2
  """
  r = move(n, 8, 6)
  r |= move(n, 7, 7)
  r |= move(n, 6, 8)
  r |= move(n, 5, 3)
  r |= move(n, 4, 4)
  r |= move(n, 3, 5)
  r |= move(n, 2, 0)
  r |= move(n, 1, 1)
  r |= move(n, 0, 2)
  return r

def rotateRight3(n):
  """
  876
  543
  210

  8 -> 6
  6 -> 0
  0 -> 2
  2 -> 8
  7 -> 3
  3 -> 1
  1 -> 5
  5 -> 7
  4 -> 4
  """
  r = move(n, 8, 6)
  r |= move(n, 6, 0)
  r |= move(n, 0, 2)
  r |= move(n, 2, 8)
  r |= move(n, 7, 3)
  r |= move(n, 3, 1)
  r |= move(n, 1, 5)
  r |= move(n, 5, 7)
  r |= move(n, 4, 4)
  return r

with open(sys.argv[1], mode="rt", encoding="utf-8") as f:
  for line in f:
    line = line.strip().replace("/", "").replace(".", "0").replace("#", "1")
    start, end = line.split(" => ")
    start = int(start, 2)
    end = int(end, 2)

    if len(line) == 17:
      replaceTwo[start] = end
      replaceTwo[rotateRight2(start)] = end
      replaceTwo[rotateRight2(rotateRight2(start))] = end
      replaceTwo[rotateRight2(rotateRight2(rotateRight2(start)))] = end
      replaceTwo[flipHoriz2(start)] = end
      replaceTwo[rotateRight2(flipHoriz2(start))] = end
      replaceTwo[rotateRight2(rotateRight2(flipHoriz2(start)))] = end
      replaceTwo[rotateRight2(rotateRight2(rotateRight2(flipHoriz2(start))))] = end

      # replaceTwo[flipVert2(start)] = end
      # replaceTwo[flipHoriz2(start)] = end
      # replaceTwo[rotateLeft2(start)] = end
      # replaceTwo[rotateRight2(start)] = end
      # replaceTwo[rotateRight2(rotateRight2(start))] = end
    else:
      replaceThree[start] = end
      replaceThree[rotateRight3(start)] = end
      replaceThree[rotateRight3(rotateRight3(start))] = end
      replaceThree[rotateRight3(rotateRight3(rotateRight3(start)))] = end
      replaceThree[flipHoriz3(start)] = end
      replaceThree[rotateRight3(flipHoriz3(start))] = end
      replaceThree[rotateRight3(rotateRight3(flipHoriz3(start)))] = end
      replaceThree[rotateRight3(rotateRight3(rotateRight3(flipHoriz3(start))))] = end

      # replaceThree[start] = end
      # replaceThree[flipVert3(start)] = end
      # replaceThree[flipHoriz3(start)] = end
      # replaceThree[rotateLeft3(start)] = end
      # replaceThree[rotateRight3(start)] = end
      # replaceThree[rotateLeft3(rotateLeft3(start))] = end

def process2x2(orig):
  newImg = []

  size = len(orig) // 2

  for y in range(size):
    newImg.append(0)
    newImg.append(0)
    newImg.append(0)

    for x in range(size):
      needle = 0
      for sourceRow in range(y * 2, y * 2 + 2):
        needle <<= 2
        needle |= orig[sourceRow] & (0b11 << ((size - x - 1) * 2))
      needle >>= 2 * (size - x - 1)
      replace = replaceTwo[needle]

      newImg[y * 3] <<= 3
      newImg[y * 3] |= (replace & 0b111_000_000) >> 6

      newImg[y * 3 + 1] <<= 3
      newImg[y * 3 + 1] |= (replace & 0b000_111_000) >> 3

      newImg[y * 3 + 2] <<= 3
      newImg[y * 3 + 2] |= replace & 0b000_000_111

  return newImg

def process3x3(orig):
  newImg = []

  size = len(orig) // 3

  for y in range(size):
    newImg.append(0)
    newImg.append(0)
    newImg.append(0)
    newImg.append(0)

    for x in range(size):
      needle = 0
      for sourceRow in range(y * 3, y * 3 + 3):
        needle <<= 3
        needle |= orig[sourceRow] & (0b111 << ((size - x - 1) * 3))
      needle >>= 3 * (size - x - 1)
      replace = replaceThree[needle]

      newImg[y * 4] <<= 4
      newImg[y * 4] |= (replace & 0xF000) >> 12

      newImg[y * 4 + 1] <<= 4
      newImg[y * 4 + 1] |= (replace & 0x0F00) >> 8

      newImg[y * 4 + 2] <<= 4
      newImg[y * 4 + 2] |= (replace & 0x00F0) >> 4

      newImg[y * 4 + 3] <<= 4
      newImg[y * 4 + 3] |= replace & 0x000F

  return newImg

for i in range(18):
  if size % 2 == 0:
    image = process2x2(image)
    size = size // 2 * 3
  elif size % 3 == 0:
    image = process3x3(image)
    size = size // 3 * 4
  else:
    assert False

popcount = 0

for row in image:
  popcount += row.bit_count()

print(popcount)
