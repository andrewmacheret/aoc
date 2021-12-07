#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 26             jq -R -r --argjson days 18 -f main.jq input-test-1
test 362740         jq -R -r --argjson days 80 -f main.jq input-real

test 26984457539    jq -R -r --argjson days 256 -f main.jq input-test-1
test 1644874076764  jq -R -r --argjson days 256 -f main.jq input-real
