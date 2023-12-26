#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 13        jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 6256        jq -R -r -s --argjson part 0  -f main.jq input-real
test 1        jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 36        jq -R -r -s --argjson part 1  -f main.jq input-test-2
test 2665        jq -R -r -s --argjson part 1  -f main.jq input-real

