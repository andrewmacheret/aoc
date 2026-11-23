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

end Common.Util
