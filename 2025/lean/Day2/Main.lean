import Common.Io
import Common.Util
import Common.Test
import Std.Data.HashSet

open Std
open Common.Io
open Common.Util
open Common.Test

def parseRange (s : String) : Nat × Nat :=
  match (s.splitOn "-").map (·.toNat!) with
  | [lo, hi] => (lo, hi)
  | _ => (0, 0)

def parseRanges (lines : Array String) : Array (Nat × Nat) :=
  ((lines[0]!.splitOn ",").map parseRange).toArray

def hasOddDigits (x : Nat) : Bool := (toString x).length % 2 == 1

def splitByLength (lo hi : Nat) : Array (Nat × Nat) := Id.run do
  let mut res := #[]
  let mut curr := lo
  while curr <= hi do
    let nextHi := min hi (repeatChar (toString curr).length '9').toNat!
    res := res.push (curr, nextHi)
    curr := nextHi + 1
  return res

def firstPart (i size : Nat) : Nat :=
  let s := toString i
  (s.take (s.length / size)).copy.toNat!

def countAnswers (lo hi part : Nat) : Id Nat := do
  let mut found : HashSet Nat := ∅
  let n := (toString hi).length
  for i in [2 : if part == 1 then 3 else n+1] do
    if n % i == 0 then
      for x in [firstPart lo i : (firstPart hi i) + 1] do
        let xx := (repeatString (toString x) i).toNat!
        if lo <= xx && xx <= hi then found := found.insert xx
  return sum found.toArray

def solve (part : Nat) (lines : Array String) : Nat :=
  let ranges := parseRanges lines
  let subRanges := ranges.flatMap fun r => splitByLength r.1 r.2
  let values := subRanges.map fun r => countAnswers r.1 r.2 part
  sum values

def main : IO Unit := do
  test 1227775554 (solve 1 (<- readLines "Day2/input-test1.txt"))
  test 40055209690 (solve 1 (<- readLines "Day2/input.txt"))
  test 4174379265 (solve 2 (<- readLines "Day2/input-test1.txt"))
  test 50857215650 (solve 2 (<- readLines "Day2/input.txt"))
