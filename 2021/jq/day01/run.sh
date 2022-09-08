#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 7            jq -r -s --argjson part 1  -f main.jq input-test-1
test 1215         jq -r -s --argjson part 1  -f main.jq input-real

test 5            jq -r -s --argjson part 2  -f main.jq input-test-1
test 1150         jq -r -s --argjson part 2  -f main.jq input-real
