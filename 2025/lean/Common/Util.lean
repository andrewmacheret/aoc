namespace Common.Util

def accumulate {α β : Type} (ints : Array α) (init : β) (op : β -> α -> β) : Array β :=
  (ints.foldl (init := (init, #[])) fun (acc, out) x =>
    let next := op acc x
    (next, out.push next)
  ).2

def repeatChar (n : Nat) (c : Char) : String :=
  String.ofList (List.replicate n c)

def repeatString (s : String) (n : Nat) : String :=
  String.join (List.replicate n s)

def sum {α : Type} [Add α] [OfNat α 0] (s : Array α) : α :=
  s.foldl (init := 0) (· + ·)


def bisectLeftBy {α β : Type} (as : Array α) (k : β) (lt : α → β → Bool) : Nat := Id.run do
  let mut lo := 0
  let mut hi := as.size
  while lo < hi do
    let mid := (lo + hi) / 2
    match as[mid]? with
    | some v =>
      if lt v k then
        lo := mid + 1
      else
        hi := mid
    | none => break
  return lo

def bisectRightBy {α β : Type} (as : Array α) (k : β) (lt : β → α → Bool) : Nat := Id.run do
  let mut lo := 0
  let mut hi := as.size
  while lo < hi do
    let mid := (lo + hi) / 2
    match as[mid]? with
    | some v =>
      if lt k v then
        hi := mid
      else
        lo := mid + 1
    | none => break
  return lo

end Common.Util
