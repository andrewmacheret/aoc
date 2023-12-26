#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 13       jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 22193    jq -R -r -s --argjson part 0  -f main.jq input-real

test 30       jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 5625994  jq -R -r -s --argjson part 1  -f main.jq input-real

