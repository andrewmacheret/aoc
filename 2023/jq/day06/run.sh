#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 288         jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 2612736     jq -R -r -s --argjson part 0  -f main.jq input-real

test 71503       jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 29891250    jq -R -r -s --argjson part 1  -f main.jq input-real
