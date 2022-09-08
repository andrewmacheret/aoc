#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 0     jq -R -r -s --argjson steps 1   -f main.jq input-test-1
test 35    jq -R -r -s --argjson steps 2   -f main.jq input-test-1
test 80    jq -R -r -s --argjson steps 3   -f main.jq input-test-1
test 204   jq -R -r -s --argjson steps 10  -f main.jq input-test-1
test 1656  jq -R -r -s --argjson steps 100 -f main.jq input-test-1
test 1700  jq -R -r -s --argjson steps 100 -f main.jq input-real

test 195   jq -R -r -s --argjson steps 200 -f main.jq input-test-1
test 273   jq -R -r -s --argjson steps 999 -f main.jq input-real
