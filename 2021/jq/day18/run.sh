#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 4140        jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 4116        jq -R -r -s --argjson part 1  -f main.jq input-real
test 3993        jq -R -r -s --argjson part 2  -f main.jq input-test-1
test 4638        jq -R -r -s --argjson part 2  -f main.jq input-real

