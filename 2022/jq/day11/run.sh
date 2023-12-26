#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 10605        jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 56595        jq -R -r -s --argjson part 0  -f main.jq input-real
test 2713310158   jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 15693274740  jq -R -r -s --argjson part 1  -f main.jq input-real

