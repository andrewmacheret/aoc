#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'  jq -R -r -s --argjson part 1 -f main.jq input-test-1.txt
test '1219070632396864'  jq -R -r -s --argjson part 1 -f main.jq input-test-2.txt
test '1125899906842624'  jq -R -r -s --argjson part 1 -f main.jq input-test-3.txt
test '2171728567'        jq -R -r -s --argjson part 1 -f main.jq input.txt

test '49815'  jq -R -r -s --argjson part 2 -f main.jq input.txt
