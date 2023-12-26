#!/usr/bin/env python3

from common.util import *
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count


def dfs(costs, mins):
  da_cost_a, db_cost_a, dc_cost_a, dc_cost_b, dd_cost_a, dd_cost_c = costs
  max_a = max(da_cost_a, db_cost_a, dc_cost_a, dd_cost_a)

  @cache
  def dfs_rec(mins, da, db, dc, dd, a, b, c, d):

    if mins == 0:
      return d  # return geodes

    a += da  # ore
    b += db  # clay
    c += dc  # obsidian
    d += dd  # geodes

    # dont keep resources that can't be spent
    a = min(a, max_a * mins)
    b = min(b, dc_cost_b * mins)
    c = min(c, dd_cost_c * mins)

    res = []
    # always buy geode bots if can afford it
    if a >= dd_cost_a+da and c >= dd_cost_c+dc and mins > 1:
      res.append(dfs_rec(mins-1, da, db, dc, dd + 1,
                         a-dd_cost_a, b, c-dd_cost_c, d))
    # else buy obs bot if can afford it and we dont have too many obs bots
    elif a >= dc_cost_a+da and b >= dc_cost_b+db and dc < dd_cost_c and mins > 3:
      res.append(dfs_rec(mins-1, da, db, dc+1, dd,
                         a-dc_cost_a, b-dc_cost_b, c, d))
      # try waiting if we dont have too much ore
      if a < max_a * 2:
        res.append(dfs_rec(mins-1, da, db, dc, dd, a, b, c, d))
    # else try other bots...
    else:
      # try buying a clay bot if we can afford it and we dont have too many clay bots
      if a >= db_cost_a+da and db < dc_cost_b and mins > 5:
        res.append(dfs_rec(mins-1, da, db + 1, dc, dd,
                           a-db_cost_a, b, c, d))
      # try buying an ore bot if we can afford it and we dont have too many ore bots
      if a >= da_cost_a+da and da < max_a and mins > 5:
        res.append(dfs_rec(mins-1, da+1, db, dc, dd,
                           a-da_cost_a, b, c, d))
      # try waiting if we dont have too much ore
      if a < max_a * 2 or not res:
        res.append(dfs_rec(mins-1, da, db, dc, dd, a, b, c, d))
    return max(res)

  return dfs_rec(mins, 1, 0, 0, 0, 0, 0, 0, 0)


def solve(part, file):
  blueprints = [tuple(parse_nums(line)[1:]) for line in load(file)]
  if part:
    blueprints = blueprints[:3]
  limit = (24, 32)[part]

  executor = ProcessPoolExecutor(max_workers=cpu_count())
  processes = [executor.submit(dfs, costs, limit)
               for costs in blueprints]
  results = [t.result() for t in processes]
  print(results)

  if part == 0:
    return sum(starmap(mul, enumerate(results, 1)))
  else:
    return reduce(mul, results)


def run_all(part):
  blueprints = []
  for costs in product(range(2, 5), range(2, 5), range(2, 5), range(5, 21), range(2, 5), range(5, 21)):
    blueprints.append(costs)
  print(len(blueprints))
  # blueprints = blueprints[:100]
  limit = (24, 32)[part]

  executor = ProcessPoolExecutor(max_workers=cpu_count())
  processes = [executor.submit(dfs, costs, limit) for costs in blueprints]
  results = []
  cheat = {}
  for i, t in enumerate(processes):
    if i % 100 == 0 and i:
      print(i)
    val = t.result()
    results.append(val)
    cheat[blueprints[i]] = val

  print(cheat)

  if part == 0:
    return sum(starmap(mul, enumerate(results, 1)))
  else:
    return reduce(mul, results)


### THE REST IS TESTS ###


if __name__ == "__main__":
  change_dir(__file__)

  test(33, solve(part=0, file='input-test-1'))
  test(2160, solve(part=0, file='input-real'))

  test(56*62, solve(part=1, file='input-test-1'))
  test(13340, solve(part=1, file='input-real'))

  # test(987567072, run_all(part=0))
