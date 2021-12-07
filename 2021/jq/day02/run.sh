#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 150        jq -R -r -s --argjson part 1 -f main.jq input-test-1
test 1746616    jq -R -r -s --argjson part 1 -f main.jq input-real

test 900        jq -R -r -s --argjson part 2 -f main.jq input-test-1
test 1741971043 jq -R -r -s --argjson part 2 -f main.jq input-real
