#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 161        jq -R -r -s --argjson part 0 -f main.jq input-test-1
test 184122457  jq -R -r -s --argjson part 0 -f main.jq input-real
# test 48         jq -R -r -s --argjson part 1 -f main.jq input-test-2
# test 107862689  jq -R -r -s --argjson part 1 -f main.jq input-real
