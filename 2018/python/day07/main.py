import re
from collections import OrderedDict
from heapq import heappush, heappop
from itertools import chain

def parse_dependencies(lines):
  # 'Step C must be finished before step A can begin.',
  # C -> A
  # C is the dependency
  # A is the user
  return [re.match(r'^Step (.+) must be finished before step (.+) can begin\.$', line).groups() for line in lines]

def order_of_steps_with_workers(dependencies, workers, base_time):
  tasks = sorted(set(chain((d for d, u in dependencies), (u for d, u in dependencies))))
  
  dependencies_by_user = OrderedDict((t, set()) for t in tasks)
  users_by_dependency = OrderedDict((t, set()) for t in tasks)
  for d, u in dependencies:
    dependencies_by_user[u].add(d)
    users_by_dependency[d].add(u)

  q = [(0, None, []) for i in xrange(workers)]
  
  while q:
    # grab a ready worker
    start, task_finished, tasks_unlocked = heappop(q)

    # keep track of when tasks finished
    if task_finished: yield (task_finished, start)

    # resolve any dependencies waiting on this worker to finish
    for u, d in tasks_unlocked:
      dependencies_by_user[u].remove(d)

    # choose the next available task
    user = next((u for u, d in dependencies_by_user.iteritems() if not d), None)
    
    # if there's no available task, put the worker in the idle queue
    if not user: continue

    # delete the dependencies for this task - it's an empty list
    del dependencies_by_user[user]

    # figure out when the worker will be done
    end = start + base_time + ord(user) - ord(tasks[0]) + 1
    
    # figure out what other tasks will unlock when this task is finished
    tasks_unlocked = [(u, user) for u in users_by_dependency[user]]

    # put the worker back on the queue with a new task
    heappush(q, (end, user, tasks_unlocked))

    # also, fill the queue back up to the maximum number of workers
    while len(q) < workers:
      heappush(q, (start, None, []))


class Day07:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.instructions = parse_dependencies(self.lines)
    return self

  def part1(self):
    return ''.join(task for task, time in order_of_steps_with_workers(self.instructions, 1, 0))

  def part2(self, workers, base_time):
    return [time for task, time in order_of_steps_with_workers(self.instructions, workers, base_time)][-1]

  def solve(self, workers, base_time):
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2(workers, base_time)}
    ]

if __name__== "__main__":
  print(Day07().load('input-test.txt').solve(2, 0))
  print(Day07().load('input.txt').solve(5, 60))
