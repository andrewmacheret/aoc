
"""
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.


A: C
B: A
C
D: A
E: B, D, F
F: C



A: C
B: A
C
D: A
E: B, D, F
F: C

generate a map of letters -> set of dependencies
generate a map of letters -> set of users

perform n times:
1. loop through until finding an empty letter
2. remove that letter and add to result
3. remove that letter from all sets that contain it
"""

from collections import OrderedDict, deque
import heapq

def parse(instructions):
  # 'Step C must be finished before step A can begin.',
  # C -> A
  # C is the dependency
  # A is the user
  parsed = []
  for instruction in instructions:
    parts = instruction.split(' ')
    parsed.append((parts[1], parts[7]))
  return parsed
  

def solve(instructions, workers, base):
  parsed = parse(instructions)
  #print(parsed)

  tasks = sorted(set([d for d, u in parsed] + [u for d, u in parsed]))
  dependencies_by_user = OrderedDict()
  users_by_dependency = {}
  for task in tasks:
    dependencies_by_user[task] = set()
    users_by_dependency[task] = set()
  for d, u in parsed:
    dependencies_by_user[u].add(d)
    users_by_dependency[d].add(u)
  #print(dependencies_by_user)
  #print(users_by_dependency)

  end_time = 0
  q = [(0, i, []) for i in xrange(workers)]
  heapq.heapify(q)
  idle_q = deque()
  while q:
    start, index, delayed = heapq.heappop(q)
    for u, d in delayed:
      print('{0}: removing {1} <- {2}'.format(start, u, d))
      dependencies_by_user[u].remove(d)

    found = False
    for user, dependencies in dependencies_by_user.iteritems():
      if not dependencies:
        found = True
        break
    if not found:
      print('{0}: nothing for worker {1} to do, going to idle q'.format(start, index))
      idle_q.append(i)
      continue
    elif idle_q:
      new_worker = idle_q.pop()
      print('{0}: putting {1} back into the queue'.format(start, new_worker))
      heapq.heappush(q, (start, new_worker, []))

    del dependencies_by_user[user]

    time = base + ord(user) - ord(tasks[0]) + 1
    end = start + time
    print('{0}: giving {1} to worker {2}, will finish at {3}'.format(start, user, index, end))
    if end_time < end: end_time = end

    delayed = []
    for u in users_by_dependency[user]:
      #at time: dependencies_by_user[u].remove(user)
      print('{0}: delaying removing {1} <- {2} until {3}'.format(start, u, user, end))
      delayed.append((u, user))
    heapq.heappush(q, (end, index, delayed))


  #print(end_time)
  return end_time



instructions = [
  'Step C must be finished before step A can begin.',
  'Step C must be finished before step F can begin.',
  'Step A must be finished before step B can begin.',
  'Step A must be finished before step D can begin.',
  'Step B must be finished before step E can begin.',
  'Step D must be finished before step E can begin.',
  'Step F must be finished before step E can begin.',
]
print(solve(instructions, 2, 0))
instructions = [
  'Step A must be finished before step R can begin.',
  'Step J must be finished before step B can begin.',
  'Step D must be finished before step B can begin.',
  'Step X must be finished before step Z can begin.',
  'Step H must be finished before step M can begin.',
  'Step B must be finished before step F can begin.',
  'Step Q must be finished before step I can begin.',
  'Step U must be finished before step O can begin.',
  'Step T must be finished before step W can begin.',
  'Step V must be finished before step S can begin.',
  'Step N must be finished before step P can begin.',
  'Step P must be finished before step O can begin.',
  'Step E must be finished before step C can begin.',
  'Step F must be finished before step O can begin.',
  'Step G must be finished before step I can begin.',
  'Step Y must be finished before step Z can begin.',
  'Step M must be finished before step K can begin.',
  'Step C must be finished before step W can begin.',
  'Step L must be finished before step W can begin.',
  'Step W must be finished before step S can begin.',
  'Step Z must be finished before step O can begin.',
  'Step K must be finished before step S can begin.',
  'Step S must be finished before step R can begin.',
  'Step R must be finished before step I can begin.',
  'Step O must be finished before step I can begin.',
  'Step A must be finished before step Q can begin.',
  'Step Z must be finished before step R can begin.',
  'Step T must be finished before step R can begin.',
  'Step M must be finished before step O can begin.',
  'Step Q must be finished before step Z can begin.',
  'Step V must be finished before step C can begin.',
  'Step Y must be finished before step W can begin.',
  'Step N must be finished before step F can begin.',
  'Step J must be finished before step D can begin.',
  'Step D must be finished before step N can begin.',
  'Step B must be finished before step M can begin.',
  'Step P must be finished before step I can begin.',
  'Step W must be finished before step Z can begin.',
  'Step Q must be finished before step V can begin.',
  'Step V must be finished before step K can begin.',
  'Step B must be finished before step Z can begin.',
  'Step M must be finished before step I can begin.',
  'Step G must be finished before step C can begin.',
  'Step K must be finished before step O can begin.',
  'Step E must be finished before step O can begin.',
  'Step C must be finished before step I can begin.',
  'Step X must be finished before step G can begin.',
  'Step B must be finished before step T can begin.',
  'Step B must be finished before step I can begin.',
  'Step E must be finished before step F can begin.',
  'Step N must be finished before step K can begin.',
  'Step D must be finished before step W can begin.',
  'Step R must be finished before step O can begin.',
  'Step V must be finished before step I can begin.',
  'Step T must be finished before step O can begin.',
  'Step B must be finished before step Q can begin.',
  'Step T must be finished before step L can begin.',
  'Step M must be finished before step C can begin.',
  'Step A must be finished before step M can begin.',
  'Step F must be finished before step L can begin.',
  'Step X must be finished before step T can begin.',
  'Step G must be finished before step K can begin.',
  'Step C must be finished before step L can begin.',
  'Step D must be finished before step Z can begin.',
  'Step H must be finished before step L can begin.',
  'Step P must be finished before step Z can begin.',
  'Step A must be finished before step V can begin.',
  'Step G must be finished before step R can begin.',
  'Step E must be finished before step G can begin.',
  'Step D must be finished before step P can begin.',
  'Step X must be finished before step L can begin.',
  'Step U must be finished before step C can begin.',
  'Step Z must be finished before step K can begin.',
  'Step E must be finished before step W can begin.',
  'Step B must be finished before step Y can begin.',
  'Step J must be finished before step I can begin.',
  'Step U must be finished before step P can begin.',
  'Step Y must be finished before step L can begin.',
  'Step N must be finished before step L can begin.',
  'Step L must be finished before step S can begin.',
  'Step H must be finished before step P can begin.',
  'Step P must be finished before step S can begin.',
  'Step J must be finished before step S can begin.',
  'Step J must be finished before step U can begin.',
  'Step H must be finished before step T can begin.',
  'Step L must be finished before step I can begin.',
  'Step N must be finished before step Z can begin.',
  'Step A must be finished before step G can begin.',
  'Step H must be finished before step S can begin.',
  'Step S must be finished before step I can begin.',
  'Step H must be finished before step E can begin.',
  'Step W must be finished before step R can begin.',
  'Step B must be finished before step G can begin.',
  'Step U must be finished before step Y can begin.',
  'Step J must be finished before step G can begin.',
  'Step M must be finished before step L can begin.',
  'Step G must be finished before step Z can begin.',
  'Step N must be finished before step W can begin.',
  'Step D must be finished before step E can begin.',
  'Step A must be finished before step W can begin.',
  'Step G must be finished before step Y can begin.',
]
print(solve(instructions, 5, 60))
