#!/usr/bin/env python3

from collections import defaultdict
import re

from common.util import load_blocks, test, change_dir


def solve(part, file):
  data = [*load_blocks(file)]
  guesses = [*map(int, data[0][0].split(","))]
  boards = [[*map(int, re.findall(r'[0-9]+', ' '.join(board)))]
            for board in data[1:]]

  rows = defaultdict(list)
  for i, board in enumerate(boards):
    for j in range(5):
      # horizontal
      for x in (s := set(board[j*5:j*5+5])):
        rows[x] += (i, s),
      # vertical
      for x in (s := set(board[j::5])):
        rows[x] += (i, s),

  played = set()
  winners = set()
  scores = []

  for guess in guesses:
    played.add(guess)
    for i, row in rows[guess]:
      row.remove(guess)
      if not row and i not in winners:
        winners.add(i)
        unused = sum(x for x in boards[i] if x not in played)
        scores += unused * guess,

  return scores[-(part - 1)]  # 0 if part 1, -1 if part 2


if __name__ == "__main__":
  change_dir(__file__)

  test(4512, solve(part=1, file='input-test-1'))
  test(21607, solve(part=1, file='input-real'))

  test(1924, solve(part=2, file='input-test-1'))
  test(19012, solve(part=2, file='input-real'))
