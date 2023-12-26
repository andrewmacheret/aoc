#!/usr/bin/env python3

from common.util import *

def combos(s, nums):
  @cache
  def fn(i=0, j=0, size=0):
    if i == len(s):
      return (j == len(nums) - 1 and size == nums[j]) \
          or (j == len(nums) and size == 0)
    m = 0
    if s[i] in '.?':
      if size == 0: # no block yet
        m += fn(i+1, j, 0)
      elif j < len(nums) and size == nums[j]: # end of block
        m += fn(i+1, j+1, 0)
    if s[i] in '#?':
      if j < len(nums) and size < nums[j]: # continue a block
        m += fn(i+1, j, size+1)
    return m
  return fn()

def solve(part, file):
  res = 0
  for line in load(file):
    s, nums = line.split(' ')
    nums = tuple(map(int, nums.split(',')))
    if part:
      s = '?'.join([s] * 5)
      nums = nums * 5
    res += combos(s, nums)
  return res


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  # test(21, solve(part=0, file='input-test-1'))
  # test(7251, solve(part=0, file='input-real'))

  # test(525152, solve(part=1, file='input-test-1'))
  test(2128386729962, solve(part=1, file='input-real'))
