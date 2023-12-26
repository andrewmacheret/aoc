#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 2                 jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 6                 jq -R -r -s --argjson part 0  -f main.jq input-test-2
test 14893             jq -R -r -s --argjson part 0  -f main.jq input-real

test 6                 jq -R -r -s --argjson part 1  -f main.jq input-test-3
test 10241191004509    jq -R -r -s --argjson part 1  -f main.jq input-real
