#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 24000        jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 68923        jq -R -r -s --argjson part 1  -f main.jq input-real
test 200044       jq -R -r -s --argjson part 2  -f main.jq input-real

