import Common.Io
import Common.Util
import Common.Test

def safe_mod (x : Int) (mod : Int) : Int := ((x % mod) + mod) % mod

def ticks1 (start _ : Int) : Int :=
  if start = 0 then 1 else 0

def ticks2 (start move : Int) : Int :=
  match compare move 0 with
  | .gt => (start + move).ediv 100
  | .lt => (((100 - start).emod 100) - move).ediv 100
  | .eq => 0

def simulate (lines : Array String) (ticks : Int -> Int -> Int) : Int :=
  let vals := lines.map fun s =>
    (let c := s.toSlice.front
    ((if c == 'L' then -1 else 1) * (s.drop 1).toInt!))
  let dials := vals.foldl
    (init := (0, 50))
    (
      fun z x => (z.1 + ticks z.2 x,
      (safe_mod (z.2 + x) 100))
    )
  dials.1

def solve1 (lines : Array String) : Int := simulate lines ticks1
def solve2 (lines : Array String) : Int := simulate lines ticks2


def main : IO Unit := do
  Common.Test.test 3 (solve1 (<- Common.Io.readLines "Day1/input-test1.txt"))
  Common.Test.test 1052 (solve1 (<- Common.Io.readLines "Day1/input.txt"))
  Common.Test.test 6 (solve2 (<- Common.Io.readLines "Day1/input-test1.txt"))
  Common.Test.test 6295 (solve2 (<- Common.Io.readLines "Day1/input.txt"))
