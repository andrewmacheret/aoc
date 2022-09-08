include "../common/util";

def hex_to_binary:
  . as $char
  | "0123456789ABCDEF"
  | index($char)
  | (8,4,2,1) as $x
  | (. / $x | floor) % 2
;

def parse:
  if .pos < (.bin | length) then
    def read($x):
      .val = (.bin[.pos:(.pos + $x)] | from_radix(2))
      | .pos += $x
    ;
    def parts($type):
      .pos as $id
      | if $type == 4 then
          reduce_while_plus_1(
            .bin[.pos] == 1;
            read(1) | read(4) | .parts[$id] += [.val]
          )
        else
          read(1)
          | if .val == 1 then
              read(11)
              | reduce range(.val) as $i (.; parse | .parts[$id] += [.res])
            else
              read(15)
              | (.pos + .val) as $last
              | reduce_while(.pos < $last; parse | .parts[$id] += [.res])
            end
        end
      | .res = (.parts[$id] | [add, mul, min, max, from_radix(16), gt, lt, eq][$type])
    ;
    read(3)
    | .versions += .val
    | read(3)
    | parts(.val)
  else . end
;

lines[0]
  | split("")
  | map(hex_to_binary)
  | {versions: 0, pos: 0, bin: .}
  | parse
  | if $part == 1 then .versions else .res end
