#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  nodes = {}
  all_children = set()
  for line in load(file):
    name, val, children_str = re.fullmatch(
        r'(.*) \((.*)\)(?: -> (.*))?', line).groups()
    children = children_str.split(', ') if children_str else []
    nodes[name] = (int(val), children)
    all_children.update(children)
  root = next(iter(set(nodes) - all_children))
  if not part:
    return root

  correct = -1

  def child_weights(name):
    nonlocal correct
    weight, children = nodes[name]
    sub_weights = [child_weights(child) for child in children]
    weight_counts = Counter(sub_weights)
    if len(weight_counts) > 1:
      x = next(x for (x, c) in weight_counts.items() if c == 1)
      i = sub_weights.index(x)
      del weight_counts[x]
      y = next(iter(weight_counts))
      weight_counts[y] += 1
      sub_weights[i] = y
      correct = nodes[children[i]][0] - x + y
    return weight + sum(sub_weights)

  child_weights(root)
  return correct


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test('tknk', solve(part=0, file='input-test-1'))
  test('wiapj', solve(part=0, file='input-real'))

  test(60, solve(part=1, file='input-test-1'))
  test(1072, solve(part=1, file='input-real'))
