import Common.Io
import Common.Util
import Common.Test

open Common.Io
open Common.Util
open Common.Test

def mergeRanges (ranges : Array (Nat × Nat)) : Array (Nat × Nat) :=
  ranges.foldl (init := #[]) fun finalRanges (a2, b2) =>
    if let some (a1, b1) := finalRanges.back?.filter (a2 <= ·.2) then
      finalRanges.pop.push (a1, max b1 b2)
    else
      finalRanges.push (a2, b2)

def solve (part : Nat) (lines : Array String) : Nat := Id.run do
  let mut ranges : Array (Nat × Nat) := #[]
  let mut query := false
  let mut count := 0
  for line in lines do
    if line.isEmpty then
      query := true
      ranges := ranges.qsort fun a b => a.1 < b.1 || (a.1 == b.1 && a.2 < b.2)
      ranges := mergeRanges ranges
      if part == 2 then
        return sum (ranges.map fun (a, b) => b - a + 1)
    else
      if !query then
        if let [a, b] := line.splitOn "-" then
          ranges := ranges.push (a.toNat!, b.toNat!)
      else
        let x := line.toNat!
        let idx := bisectLeftBy ranges x (fun (_a, b) target => b < target)
        if ranges[idx]?.any fun (a, b) => (a <= x && x <= b) then
          count := count + 1
  return count

def main : IO Unit := do
  test 3                 (solve 1 (<- readLines "Day5/input-test1.txt"))
  test 511               (solve 1 (<- readLines "Day5/input.txt"))
  test 14                (solve 2 (<- readLines "Day5/input-test1.txt"))
  test 350939902751909   (solve 2 (<- readLines "Day5/input.txt"))
