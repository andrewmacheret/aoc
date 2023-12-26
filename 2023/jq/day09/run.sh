#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 114          jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 1868368343   jq -R -r -s --argjson part 0  -f main.jq input-real

test 2            jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 1022         jq -R -r -s --argjson part 1  -f main.jq input-real
