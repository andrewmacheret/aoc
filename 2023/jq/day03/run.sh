#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 4361      jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 529618    jq -R -r -s --argjson part 0  -f main.jq input-real

test 467835    jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 77509019  jq -R -r -s --argjson part 1  -f main.jq input-real
