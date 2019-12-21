#!/usr/bin/env python3
from itertools import islice, chain, repeat, cycle

from day01.main import load, test

PATTERN = [0, 1, 0, -1]

def to_digits(s):
  return list(map(int, str(s)))

def to_str(digits):
  return ''.join(map(str, digits))

def load_digits(filename, script=__file__):
  return next(to_digits(line) for line in load(filename, script=script))

def fft(digits, phases):
  for _ in range(phases):
    digits = [abs(sum(a*b for a,b in zip(digits, islice(chain.from_iterable(repeat(i, k) for i in cycle(PATTERN)), 1, None))))%10 for k in range(1, len(digits)+1)]
  return digits

def fft_tail(digits, phases, digits_repeat=10000):
  offset = int(to_str(digits[:7]))
  tail = (digits * digits_repeat)[offset:]
  for _ in range(phases):
    for i in range(len(tail) - 1, 0, -1):
      tail[i-1] = (tail[i-1] + tail[i]) % 10
  return tail

def part1(filename, phases):
  return fft(load_digits(filename), phases)[:8]

def part2(filename, phases):
  return fft_tail(load_digits(filename), phases)[:8]

if __name__== "__main__":
  test('01029498', to_str(part1('input-test-1.txt', 4)))
  test('24176176', to_str(part1('input-test-2.txt', 100)))
  test('73745418', to_str(part1('input-test-3.txt', 100)))
  test('52432133', to_str(part1('input-test-4.txt', 100)))
  test('28430146', to_str(part1('input.txt', 100)))

  test('84462026', to_str(part2('input-test-5.txt', 100)))
  test('78725270', to_str(part2('input-test-6.txt', 100)))
  test('53553731', to_str(part2('input-test-7.txt', 100)))
  test('12064286', to_str(part2('input.txt', 100)))
