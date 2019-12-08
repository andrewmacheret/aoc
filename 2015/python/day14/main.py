#!/usr/bin/env python3
import re

from day01.main import load, test

def load_regex(filename, regex, script=__file__):
  return [re.match(regex, line).groups() for line in load(filename, script=script)]

def load_reindeers(filename, script=__file__):
  regex = r'(.*) can fly (.*) km/s for (.*) seconds, but then must rest for (.*) seconds.'
  return [(name, list(map(int, values))) for name, *values in load_regex(filename, regex=regex, script=__file__)]

def distance_traveled(time, run_speed, run_time, rest_time):
  cycle_time = run_time + rest_time
  cycles = time // cycle_time
  return (run_time * cycles + min(time - (cycles * cycle_time), run_time)) * run_speed

def fastest_reindeer(filename, time):
  return max(distance_traveled(time, *values) for name, values in load_reindeers(filename))

def pointiest_reindeer(filename, time, op=max):
  reindeers = load_reindeers(filename)
  points = {name: 0 for name, _ in reindeers}
  for t in range(1, time+1):
    distances = [(distance_traveled(t, *values), name) for name, values in reindeers]
    furthest = max(distances)[0]
    winners = [name for distance, name in distances if distance == furthest]
    for name in winners: points[name] += 1
  return op(points.values())

if __name__== "__main__":
  test(16, fastest_reindeer('input-test-1.txt', 1))
  test(1120, fastest_reindeer('input-test-1.txt', 1000))
  test(2660, fastest_reindeer('input.txt', 2503))
  
  test(1, pointiest_reindeer('input-test-1.txt', 1))
  test(689, pointiest_reindeer('input-test-1.txt', 1000))
  test(312, pointiest_reindeer('input-test-1.txt', 1000, op=min))
  test(1256, pointiest_reindeer('input.txt', 2503))
