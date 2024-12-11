#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 7                jq -R -r -s --argjson steps 1 -f main.jq input-test-1
test 22               jq -R -r -s --argjson steps 6 -f main.jq input-test-2
test 55312            jq -R -r -s --argjson steps 25 -f main.jq input-test-2
test 202019           jq -R -r -s --argjson steps 25 -f main.jq input-real
test 239321955280205  jq -R -r -s --argjson steps 75 -f main.jq input-real
