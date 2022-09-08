#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 10     jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 19     jq -R -r -s --argjson part 1  -f main.jq input-test-2
test 226    jq -R -r -s --argjson part 1  -f main.jq input-test-3
test 3738   jq -R -r -s --argjson part 1  -f main.jq input-real

test 36     jq -R -r -s --argjson part 2  -f main.jq input-test-1
test 103    jq -R -r -s --argjson part 2  -f main.jq input-test-2
test 3509   jq -R -r -s --argjson part 2  -f main.jq input-test-3
test 120506 jq -R -r -s --argjson part 2  -f main.jq input-real
