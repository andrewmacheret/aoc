#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

# test 1320         jq -R -r -s --argjson part 0  -f main.jq input-test-1
# test 506869       jq -R -r -s --argjson part 0  -f main.jq input-real

test 145          jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 271384       jq -R -r -s --argjson part 1  -f main.jq input-real
