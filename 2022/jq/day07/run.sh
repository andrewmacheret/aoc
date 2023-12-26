#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 95437            jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 1583951          jq -R -r -s --argjson part 1  -f main.jq input-real
test 24933642         jq -R -r -s --argjson part 2  -f main.jq input-test-1
test 214171           jq -R -r -s --argjson part 2  -f main.jq input-real
