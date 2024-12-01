#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 11        jq -R -r -s --argjson part 0 -f main.jq input-test-1
test 1530215   jq -R -r -s --argjson part 0 -f main.jq input-real
test 31        jq -R -r -s --argjson part 1 -f main.jq input-test-1
test 26800609  jq -R -r -s --argjson part 1 -f main.jq input-real
