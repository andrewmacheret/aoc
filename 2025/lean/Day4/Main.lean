import Common.Io
import Common.Test

open Common.Io
open Common.Test

def DIRS_8 : List (Int × Int) := [
  (-1, -1), (-1, 0), (-1, 1),
  (0, -1), (0, 1),
  (1, -1), (1, 0), (1, 1)
]

def parseGrid (lines : Array String) : Array (Array Bool) :=
  lines.map fun line => (
      line.toList.map fun char =>
        char == '@'
    ).toArray

def count8 (grid : Array (Array Bool)) (i j : Nat) : Nat :=
  DIRS_8.countP fun (di, dj) =>
    let r := (i : Int) + di
    let c := (j : Int) + dj
    r >= 0 && c >= 0 && (grid[r.toNat]?.bind (·[c.toNat]?)).getD false

def solve (part : Nat) (lines : Array String) : Nat := Id.run do
  let initialGrid := parseGrid lines
  let mut grid : Array (Array Bool) := initialGrid
  let mut count : Nat := 0

  repeat
    let mut change : Nat := 0
    (grid, change) := (do
      grid.mapIdxM fun i row =>
        row.mapIdxM fun j val => do
          let res := val && count8 grid i j >= 4
          if val && !res then
            modify (· + 1)
          return res
      : StateT Nat Id _
    ).run 0
    if change = 0 then break
    count := count + change
    if part = 1 then break

  return count


def main : IO Unit := do
  test 13   (solve 1 (<- readLines "Day4/input-test1.txt"))
  test 1409 (solve 1 (<- readLines "Day4/input.txt"))
  test 43   (solve 2 (<- readLines "Day4/input-test1.txt"))
  test 8366 (solve 2 (<- readLines "Day4/input.txt"))
