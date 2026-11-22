namespace Common.Test

def test {α : Type} [BEq α] [ToString α] (expected actual : α) : IO Unit := do
  let result := if expected == actual then "PASS" else "FAIL"
  let expStr := toString expected
  let actStr := toString actual
  if expStr.contains '\n' then
    IO.println s!"{result} ... expected = \n{expStr}\n actual = \n{actStr}\n"
  else
    IO.println s!"{result} ... expected = {expStr} actual = {actStr}"

end Common.Test
