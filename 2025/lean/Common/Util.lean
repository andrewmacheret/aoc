namespace Common.Util

def accumulate {α β : Type} (ints : Array α) (init : β) (op : β -> α -> β) : Array β :=
  (ints.foldl (init := (init, #[])) fun (acc, out) x =>
    let next := op acc x
    (next, out.push next)
  ).2

end Common.Util
