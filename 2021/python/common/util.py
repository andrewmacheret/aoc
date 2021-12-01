import os


def load(filename):
  with open(filename) as f:
    return f.read().splitlines()


def load_ints(filename):
  return map(int, load(filename))


def test(expected, actual):
  result = ["FAIL", "PASS"][expected == actual]
  print(("{} ... expected={} actual={}").format(result, expected, actual))


def change_dir(script):
  os.chdir(os.path.dirname(script))
