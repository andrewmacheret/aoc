#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 13        jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 5330        jq -R -r -s --argjson part 0  -f main.jq input-real
test 140        jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 27648        jq -R -r -s --argjson part 1  -f main.jq input-real

