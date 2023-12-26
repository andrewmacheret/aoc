include "../common/util";

def predict:
  reduce_while(.[-1] | unique != [0];
    . + [.[-1] | pairwise | map(.[1] - .[0])]
  ) |
  reduce reverse[] as $g (0; $g[0] - .)
;

lines | map([numbers | [reverse, .][$part]] | predict) | add
