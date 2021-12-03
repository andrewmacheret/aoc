[
  split("\n")[0:-1][]
    | split(" ")
    | {dir: .[0][0:1], x: (.[1] | tonumber)}
] | reduce .[] as $i ([0,0,0]; [
      (.[0] + (if $i.dir == "f" then $i.x else 0 end)),
      (.[1] + (if $i.dir == "f" then $i.x * .[2] else 0 end)),
      (.[2] + (if $i.dir == "d" then $i.x elif $i.dir == "u" then -$i.x else 0 end))
    ]
  ) | .[0] * .[3 - ($part | tonumber)]
