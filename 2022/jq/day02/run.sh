#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 15        jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 14163     jq -R -r -s --argjson part 1  -f main.jq input-real
test 12        jq -R -r -s --argjson part 2  -f main.jq input-test-1
test 12091     jq -R -r -s --argjson part 2  -f main.jq input-real
