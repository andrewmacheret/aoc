#!/usr/bin/env python3
from threading import Thread
from datetime import datetime
from time import sleep

from day01.main import test
from day02.main import load_memory
from day05.main import Program
from day11.main import draw

class Computer():
  def __init__(self, memory, id):
    self.id = id
    self.prog = Program(memory, [id], default=-1)
    self.run = self.prog.run_computer()
  
  def start(self, notify):
    try:
      while True:
        addr = next(self.run)
        x = next(self.run)
        y = next(self.run)
        notify(self.id, addr, x, y)
    except:
      pass

def solve(filename, count=50, use_nat=True):
  memory = load_memory(filename, script=__file__)
  computers = [Computer(memory, i) for i in range(count)]

  nat_time, nat_x, nat_y = None, None, None

  def kill_all():
    for computer in computers:
      computer.prog.interrupt = True

  def notify(id, addr, x, y):
    nonlocal nat_time, nat_x, nat_y
    time = datetime.now()
    print('[{}] id={}: addr={} x={} y={}'.format(time, id, addr, x, y))
    if addr == 255:
      nat_time, nat_x, nat_y = time, x, y
      if not use_nat:
        kill_all()
    else:
      i = computers[addr].prog.input
      i.append(x)
      i.append(y)

  def nat(grace_period):
    print ('NAT booted')
    last_delivered_y = None
    while True:
      time = datetime.now()
      if nat_time is not None and (time - nat_time).seconds > grace_period:
        print('NATTACK!')
        if last_delivered_y == nat_y:
          kill_all()
          return
        last_delivered_y = nat_y
        notify(255, 0, nat_x, nat_y)
        sleep(grace_period)
      else:
        print('NATNAPPING...', nat_time and (time - nat_time).seconds)
        sleep(1)

  threads = [Thread(target=computer.start, args=(notify,)) for computer in computers]
  if use_nat: threads.append(Thread(target=nat, args=(5,)))
  for t in threads: t.start()
  for t in threads: t.join()

  return nat_y


if __name__== "__main__":
  test(17849, solve('input.txt', 50, use_nat=False))
  test(12235, solve('input.txt', 50, use_nat=True))
