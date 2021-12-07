#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 5      jq -R -r -s --argjson part 1 -f main.jq input-test-1
test 4873   jq -R -r -s --argjson part 1 -f main.jq input-real

test 12     jq -R -r -s --argjson part 2 -f main.jq input-test-1
test 19472  jq -R -r -s --argjson part 2 -f main.jq input-real
