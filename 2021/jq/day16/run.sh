#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 6            jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 9            jq -R -r -s --argjson part 1  -f main.jq input-test-2
test 14           jq -R -r -s --argjson part 1  -f main.jq input-test-3
test 16           jq -R -r -s --argjson part 1  -f main.jq input-test-4
test 12           jq -R -r -s --argjson part 1  -f main.jq input-test-5
test 23           jq -R -r -s --argjson part 1  -f main.jq input-test-6
test 31           jq -R -r -s --argjson part 1  -f main.jq input-test-7
test 1007         jq -R -r -s --argjson part 1  -f main.jq input-real


test 2021         jq -R -r -s --argjson part 2  -f main.jq input-test-1
test 1            jq -R -r -s --argjson part 2  -f main.jq input-test-2
test 3            jq -R -r -s --argjson part 2  -f main.jq input-test-3
test 15           jq -R -r -s --argjson part 2  -f main.jq input-test-4
test 46           jq -R -r -s --argjson part 2  -f main.jq input-test-5
test 46           jq -R -r -s --argjson part 2  -f main.jq input-test-6
test 54           jq -R -r -s --argjson part 2  -f main.jq input-test-7
test 3            jq -R -r -s --argjson part 2  -f main.jq input-test-8
test 54           jq -R -r -s --argjson part 2  -f main.jq input-test-9
test 7            jq -R -r -s --argjson part 2  -f main.jq input-test-10
test 9            jq -R -r -s --argjson part 2  -f main.jq input-test-11
test 1            jq -R -r -s --argjson part 2  -f main.jq input-test-12
test 0            jq -R -r -s --argjson part 2  -f main.jq input-test-13
test 0            jq -R -r -s --argjson part 2  -f main.jq input-test-14
test 1            jq -R -r -s --argjson part 2  -f main.jq input-test-15
test 834151779165 jq -R -r -s --argjson part 2  -f main.jq input-real
