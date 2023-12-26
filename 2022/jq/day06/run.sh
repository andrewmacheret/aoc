#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 7        jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 5        jq -R -r -s --argjson part 0  -f main.jq input-test-2
test 6        jq -R -r -s --argjson part 0  -f main.jq input-test-3
test 10       jq -R -r -s --argjson part 0  -f main.jq input-test-4
test 11       jq -R -r -s --argjson part 0  -f main.jq input-test-5
test 1034     jq -R -r -s --argjson part 0  -f main.jq input-real

test 19       jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 23       jq -R -r -s --argjson part 1  -f main.jq input-test-2
test 23       jq -R -r -s --argjson part 1  -f main.jq input-test-3
test 29       jq -R -r -s --argjson part 1  -f main.jq input-test-4
test 26       jq -R -r -s --argjson part 1  -f main.jq input-test-5
test 2472     jq -R -r -s --argjson part 1  -f main.jq input-real
