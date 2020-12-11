#!/usr/bin/env python3
import re

from day01.main import load, test

def passport(creds):
  return {k:v for k,v in [cred.split(":") for cred in creds]}

def load_passports(filename, script=__file__):
  creds = []
  for line in load(filename, script=script):
    if line:
      creds += line.split(" ")
    else:
      yield passport(creds)
      creds = []
  if creds:
    yield passport(creds)

def validate_simple(passport):
  return len(passport) == (8 if "cid" in passport else 7)

def validate_complex(passport):
  return bool(validate_simple(passport)
    and re.match(r'^(19[2-9][0-9]|200[0-2])$', passport['byr'])
    and re.match(r'^(201[0-9]|2020)$', passport['iyr'])
    and re.match(r'^(202[0-9]|2030)$', passport['eyr'])
    and re.match(r'^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$', passport['hgt'])
    and re.match(r'^#[0-9a-f]{6}$', passport['hcl'])
    and re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl'])
    and re.match(r'^[0-9]{9}$', passport['pid'])
  )

def part1(filename):
  P = load_passports(filename)
  return sum(map(validate_simple, P))

def part2(filename):
  P = load_passports(filename)
  return sum(map(validate_complex, P))

if __name__== "__main__":
  test(2, part1('input-test-1.txt'))
  test(247, part1('input.txt'))
  
  test(0, part2('input-test-2.txt'))
  test(3, part2('input-test-3.txt'))
  test(145, part2('input.txt'))
