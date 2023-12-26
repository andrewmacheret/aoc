#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 8         jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 2348      jq -R -r -s --argjson part 1  -f main.jq input-real

test 2286      jq -R -r -s --argjson part 2  -f main.jq input-test-1
test 76008     jq -R -r -s --argjson part 2  -f main.jq input-real
