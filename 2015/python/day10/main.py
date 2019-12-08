#!/usr/bin/env python3
import re

from day01.main import load, test

def looksee(digits):
  return ''.join(str(len(a)) + b for a, b in re.findall(r'((.)\2*)', digits))

def looksee_loop(digits, n):
  for _ in range(n): digits = looksee(digits)
  return digits

if __name__== "__main__":
  test("11", looksee("1"))
  test("21", looksee("11"))
  test("1211", looksee("21"))
  test("111221", looksee("1211"))
  test("312211", looksee("111221"))
  test("312211", looksee_loop("1", n=5))
  test(360154, len(looksee_loop("1113122113", n=40)))
  test(5103798, len(looksee_loop("1113122113", n=50)))
