#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 40      jq -R -r -s --argjson multiplier 1  -f main.jq input-test-1
test 748     jq -R -r -s --argjson multiplier 1  -f main.jq input-real

# fails
#test 315     jq -R -r -s --argjson multiplier 5  -f main.jq input-test-1

# takes too long
#test 3045    jq -R -r -s --argjson multiplier 5  -f main.jq input-real
