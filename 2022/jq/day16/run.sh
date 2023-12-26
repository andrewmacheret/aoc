#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 1651        jq -R -r -s --argjson part 1  -f main.jq input-test-1
# test 1638        jq -R -r -s --argjson part 1  -f main.jq input-real
# test 1707        jq -R -r -s --argjson part 2  -f main.jq input-test-1
# test 2400        jq -R -r -s --argjson part 2  -f main.jq input-real

