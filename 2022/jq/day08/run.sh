#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 21        jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 1538        jq -R -r -s --argjson part 1  -f main.jq input-real
test 8        jq -R -r -s --argjson part 2  -f main.jq input-test-1
test 496125        jq -R -r -s --argjson part 2  -f main.jq input-real
