import Common.Io
import Common.Util
import Common.Test
import Std.Data.HashSet

open Std
open Common.Io
open Common.Util
open Common.Test

def maxZipIdx (arr : Array Nat) : (Nat × Nat) :=
  arr.zipIdx.foldl (init := (0, 0)) fun z x => if x.1 > z.1 then x else z

def joltage (size : Nat) (line : String) : Id Nat := do
  let digits := (line.toList.map (fun c => c.toNat - '0'.toNat)).toArray
  let mut i : Nat := 0
  let mut s : String := ""
  for j in 0...size do
    let b := maxZipIdx digits[i : digits.size - size + 1 + j].toArray
    i := i + b.2 + 1
    s := s!"{s}{b.1}"
  return s.toNat!

def solve (size : Nat) (lines : Array String) : Nat :=
  sum (lines.map (joltage size ·))

def main : IO Unit := do
  test 357 (solve 2 (<- readLines "Day3/input-test1.txt"))
  test 17359 (solve 2 (<- readLines "Day3/input.txt"))
  test 3121910778619 (solve 12 (<- readLines "Day3/input-test1.txt"))
  test 172787336861064 (solve 12 (<- readLines "Day3/input.txt"))
