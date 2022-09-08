#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 1588              jq -R -r -s --argjson steps 10  -f main.jq input-test-1
test 2851              jq -R -r -s --argjson steps 10  -f main.jq input-real

test 2188189693529     jq -R -r -s --argjson steps 40  -f main.jq input-test-1
test 10002813279337    jq -R -r -s --argjson steps 40  -f main.jq input-real
