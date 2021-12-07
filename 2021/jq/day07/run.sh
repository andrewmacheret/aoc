#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 37        jq -R -r --argjson part 1 -f main.jq input-test-1
test 343441    jq -R -r --argjson part 1 -f main.jq input-real

test 168       jq -R -r --argjson part 2 -f main.jq input-test-1
test 98925151  jq -R -r --argjson part 2 -f main.jq input-real
