import re
from collections import defaultdict, Counter

import sys
sys.path.append('../')
from day03.main import multimap

def parse_logs(lines):
  id, last_asleep, sleep_times = None, None, []
  for line in sorted(lines):
    timestamp, message = re.match(r'^\[(\d+-\d+-\d+ \d+:\d+)\] (.+)$', line).groups()
    if message == 'falls asleep':
      last_asleep = timestamp
    elif message == 'wakes up':
      sleep_times.append((id, last_asleep, timestamp))
    else:
      id = re.match(r'^Guard #(\d+) begins shift$', message).group(1)
  return sleep_times

def coalesce_ranges(ranges, start, end):
  counter = Counter(start+i for s, e in ranges for i in xrange(s, e))
  return [counter[i] for i in xrange(start, end)]

def sleepiest_guard(sleep_times):
  # return the guard that spent the most time asleep
  sleep_time_per_guard = multimap((id, int(end[14:]) - int(start[14:])) for id, start, end in sleep_times)
  return max((sum(sleep_times_for_guard), id) for id, sleep_times_for_guard in sleep_time_per_guard.iteritems())

def sleepiest_minute(sleep_times, sleepiest_id):
  sleep_ranges = [(int(start[14:]), int(end[14:])) for id, start, end in sleep_times if id == sleepiest_id]
  return max((times_asleep, minute) for minute, times_asleep in enumerate(coalesce_ranges(sleep_ranges, 0, 60)))

def draw(sleep_times):
  print('Date   ID    Minute')
  print('             ' + ''.join(str(m/10) for m in xrange(60)))
  print('             ' + ''.join(str(m%10) for m in xrange(60)))
  
  sleep_time_rows = multimap(((start[:10], id), (int(start[14:]), int(end[14:]))) for id, start, end in sleep_times)
  
  for (date, id), sleep_time_row in sorted(sleep_time_rows.iteritems()):
    row = ''.join('#' if i > 0 else '.' for i in coalesce_ranges(sleep_time_row, 0, 60))
    print('{}  #{:4} {}'.format(date[5:], str(id), row))


class Day04:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.sleep_times = parse_logs(self.lines)
    return self

  def part1(self):
    id = sleepiest_guard(self.sleep_times)[1]
    minute = sleepiest_minute(self.sleep_times, id)[1]
    return int(id) * minute

  def part2(self):
    ids = set(id for id, start, end in self.sleep_times)
    (times_asleep, minute), id = max((sleepiest_minute(self.sleep_times, id), id) for id in ids)
    return int(id) * minute

  def solve(self):
    if self.verbose: draw(self.sleep_times)
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()}
    ]

if __name__== "__main__":
  print(Day04(verbose=True).load('input-test.txt').solve())
  print(Day04().load('input.txt').solve())
