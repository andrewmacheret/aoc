import Common.Io
import Common.Util
import Common.Test

def parseRange (s : String) : Nat × Nat :=
  match (s.splitOn "-").map (·.toNat!) with
  | [lo, hi] => (lo, hi)
  | _ => (0, 0)

def parseRanges (lines : Array String) : Array (Nat × Nat) :=
  ((lines[0]!.splitOn ",").map parseRange).toArray

def hasOddDigits (x : Nat) : Bool := (toString x).length % 2 == 1

def fixRange (lo hi : Nat) : Nat × Nat :=
  (
    if hasOddDigits lo then s!"1{Common.Util.repeatChar (toString lo).length '0'}".toNat! else lo,
    if hasOddDigits hi then (Common.Util.repeatChar ((toString hi).length - 1) '9').toNat! else hi
  )

def firstHalf (i : Nat) : Nat :=
  let s := toString i
  (s.take (s.length / 2)).copy.toNat!

def countAnswers (lo hi : Nat) : Id Nat := do
  let mut total := 0
  if lo < hi then
    for x in [firstHalf lo : (firstHalf hi) + 1] do
      let xx := s!"{x}{x}".toNat!
      if lo <= xx && xx <= hi then total := total + xx
  return total

def solve (lines : Array String) : Nat :=
  let ranges := parseRanges lines
  let fixedRanges := ranges.map fun r => fixRange r.1 r.2
  let values := fixedRanges.map fun r => countAnswers r.1 r.2
  values.foldl (init := 0) (· + ·)

def main : IO Unit := do
  Common.Test.test 1227775554 (solve (<- Common.Io.readLines "Day2/input-test1.txt"))
  Common.Test.test 40055209690 (solve (<- Common.Io.readLines "Day2/input.txt"))
