#!/usr/bin/env python3


from common.util import draw, load_blocks, parse_nums, test, change_dir, ocr


def solve(part, file):
  data = load_blocks(file)
  grid = set()
  for line in data[0]:
    a, b = parse_nums(line)
    grid.add((a, b))

  for line in data[1]:
    x_or_y, val = line[11], int(line[13:])
    grid2 = set()
    for x, y in grid:
      x2 = x if x_or_y == 'y' else (x if x <= val else val - (x - val))
      y2 = y if x_or_y == 'x' else (y if y <= val else val - (y - val))
      grid2.add((x2, y2))
    grid = grid2
    if part == 1:
      return len(grid)

  return draw(grid)


if __name__ == "__main__":
  change_dir(__file__)

  test(17, solve(part=1, file='input-test-1'))
  test(693, solve(part=1, file='input-real'))

  test("""
#####
#...#
#...#
#...#
#####
""", '\n' + solve(part=2, file='input-test-1') + '\n')

  test("""
#..#..##..#....####.###...##..####.#..#
#..#.#..#.#.......#.#..#.#..#....#.#..#
#..#.#....#......#..#..#.#..#...#..#..#
#..#.#....#.....#...###..####..#...#..#
#..#.#..#.#....#....#.#..#..#.#....#..#
.##...##..####.####.#..#.#..#.####..##.
""", '\n' + solve(part=2, file='input-real') + '\n')

  test("UCLZRAZU", ocr(solve(part=2, file='input-real')))
