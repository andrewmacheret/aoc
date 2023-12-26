#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test null        jq -R -r -s --argjson part 1  -f main.jq input-test-1
# test null        jq -R -r -s --argjson part 1  -f main.jq input-real
# test null        jq -R -r -s --argjson part 2  -f main.jq input-test-1
# test null        jq -R -r -s --argjson part 2  -f main.jq input-real

