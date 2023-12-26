#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 35          jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 340994526   jq -R -r -s --argjson part 0  -f main.jq input-real

test 46          jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 52210644    jq -R -r -s --argjson part 1  -f main.jq input-real
