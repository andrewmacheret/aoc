#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 198        jq -R -r -s --argjson part 1 -f main.jq input-test-1
test 3985686    jq -R -r -s --argjson part 1 -f main.jq input-real

test 230        jq -R -r -s --argjson part 2 -f main.jq input-test-1
test 2555739    jq -R -r -s --argjson part 2 -f main.jq input-real
