#!/usr/bin/env python3
from itertools import zip_longest

from day01.main import load, test

def group(iterable, n, fillvalue=None):
  args = [iter(iterable)] * n
  return zip_longest(fillvalue=fillvalue, *args)

def flatten_layer(layer):
  return [digit for row in layer for digit in row]

def print2d(grid, w, h, translate=lambda val: val):
  return '\n'.join(''.join(translate(grid[x, y]) for x in range(w)) for y in range(h))

def load_digits(filename, script=__file__):
  return [int(c) for line in load(filename, script=script) for c in line]

def create_layers(digits, w, h):
  return [list(group(layer, w)) for layer in group(digits, w * h)], w, h

def load_layers(filename, w, h, script=__file__):
  return create_layers(load_digits(filename), w, h)

def checksum(layers):
  flat = min(map(flatten_layer, layers), key=lambda f: f.count(0))
  return flat.count(1) * flat.count(2)

def merge_layers(layers, w, h):
  return {(x, y): next(layer[y][x] for layer in layers if layer[y][x] != 2) for y in range(h) for x in range(w)}, w, h

def image_to_str(image, w, h):
  return print2d(image, w, h, translate=lambda val: ' *'[val])

def part1(filename, w, h):
  return checksum(load_layers(filename, w, h)[0])

def part2(filename, w, h):
  return image_to_str(*merge_layers(*load_layers(filename, w, h)))

if __name__== "__main__":
  test(1, part1('input-test-1.txt', 3, 2))
  test(2806, part1('input.txt', 25, 6))

  test(" *\n* ", part2('input-test-2.txt', 2, 2))
  expected = """\
**** ***    **  **  ***  
   * *  *    * *  * *  * 
  *  ***     * *  * ***  
 *   *  *    * **** *  * 
*    *  * *  * *  * *  * 
**** ***   **  *  * ***  \
"""
  test(expected, part2('input.txt', 25, 6))
