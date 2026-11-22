import Common.Io
import Common.Util

def safe_mod (x : Int) (mod : Int) : Int := ((x % mod) + mod) % mod

def solve (lines : Array String) : Int :=
  0

def main : IO Unit := do
  IO.println (solve (<- Common.Io.readLines "Day2/input-test1.txt"))
  IO.println (solve (<- Common.Io.readLines "Day2/input.txt"))
