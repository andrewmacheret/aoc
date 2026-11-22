namespace Common.Util

def accumulate {α β : Type} (ints : Array α) (init : β) (op : β -> α -> β) : Array β :=
  (ints.foldl (init := (init, #[])) fun (acc, out) x =>
    let next := op acc x
    (next, out.push next)
  ).2

def repeatChar (n : Nat) (c : Char) : String :=
  String.ofList (List.replicate n c)

end Common.Util
