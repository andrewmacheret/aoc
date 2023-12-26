#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 157        jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 8394        jq -R -r -s --argjson part 1  -f main.jq input-real
test 70        jq -R -r -s --argjson part 2  -f main.jq input-test-1
test 2413        jq -R -r -s --argjson part 2  -f main.jq input-real

