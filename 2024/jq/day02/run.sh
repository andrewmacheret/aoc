#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 2        jq -R -r -s --argjson part 0 -f main.jq input-test-1
test 236      jq -R -r -s --argjson part 0 -f main.jq input-real
test 4        jq -R -r -s --argjson part 1 -f main.jq input-test-1
test 308      jq -R -r -s --argjson part 1 -f main.jq input-real


