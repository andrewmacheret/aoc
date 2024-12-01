#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test "[3500,9,10,70,2,3,11,0,99,30,40,50]"  jq -R -r -s --argjson part 0  -f main.jq input-test-1.txt
test "[2,0,0,0,99]"                         jq -R -r -s --argjson part 0  -f main.jq input-test-2.txt
test "[2,3,0,6,99]"                         jq -R -r -s --argjson part 0  -f main.jq input-test-3.txt
test "[2,4,4,5,99,9801]"                    jq -R -r -s --argjson part 0  -f main.jq input-test-4.txt
test "[30,1,1,4,2,5,6,0,99]"                jq -R -r -s --argjson part 0  -f main.jq input-test-5.txt

test 3085697  jq -R -r -s --argjson part 1  -f main.jq input.txt
test 9425     jq -R -r -s --argjson part 2  -f main.jq input.txt
