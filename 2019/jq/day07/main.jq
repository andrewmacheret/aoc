include "common/util";
include "common/prog";

def permutations:
  def rec:
    if .rest == [] then
      .picks
    else
      range(.rest | length) as $i |
      .picks += [.rest[$i]] |
      del(.rest[$i]) |
      rec
    end;
  [{picks: [], rest: .} | rec];

def init_progs($ints; $p):
  {progs: ($p | map(init_prog($ints; [.]))), i: 0, last: 0};

def chain_step:
  .progs[.i].in += [.last] |
  .progs[.i] = (.progs[.i] | step_prog) |
  .last = .progs[.i].out |
  .i = .i + 1;

def chain_once:
  (.progs | length) as $n |
  reduce_while (.i < $n; chain_step) |
  .progs[-1].out;

def chain_repeatedly:
  (.progs | length) as $n |
  reduce_while (.last != null; chain_step | .i = .i % $n) |
  .progs[-1].out;

ints as $ints |
  [
    [if $part == 1 then range(5) else range(5;10) end] | permutations[] as $p |
    (
      init_progs($ints; $p) |
      if $part == 1 then chain_once else chain_repeatedly end
    )
  ] | max
