#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 45          jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 3160        jq -R -r -s --argjson part 1  -f main.jq input-real
test 112         jq -R -r -s --argjson part 2  -f main.jq input-test-1
test 1928        jq -R -r -s --argjson part 2  -f main.jq input-real
