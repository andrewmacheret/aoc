#!/usr/bin/env python3
import re

from day01.main import load, test

def is_valid(password):
  return any(ord(a) == ord(b) - 1 == ord(c) - 2 for a, b, c in zip(password, password[1:], password[2:])) \
    and bool(re.search(r'(.)\1.*(.)\2', password)) \
    and not re.search(r'[iol]', password)

def next_password(password):
  if password[-1] == 'z':
    return next_password(password[:-1]) + 'a'
  add = 2 if password[-1] == 'h' or password[-1] == 'n' or password[-1] == 'k' else 1
  return password[:-1] + chr(ord(password[-1])+add)

def valid_passwords(password):
  while True:
    password = next_password(password)
    if is_valid(password): yield password

if __name__== "__main__":
  test(False, is_valid("hijklmmn"))
  test(False, is_valid("abbceffg"))
  test(False, is_valid("abbcegjk"))
  test(True, is_valid("abcdffaa"))
  test(True, is_valid("ghjaabcc"))
  test("abcdffaa", next(valid_passwords("abcdefgh")))
  test("ghjaabcc", next(valid_passwords("ghijklmn")))
  test("hepxxyzz", next(valid_passwords("hepxcrrq")))
  test("heqaabcc", next(valid_passwords("hepxxyzz")))
