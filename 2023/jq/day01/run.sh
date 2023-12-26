#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 142         jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 55123       jq -R -r -s --argjson part 1  -f main.jq input-real

test 281         jq -R -r -s --argjson part 2  -f main.jq input-test-2
test 55260       jq -R -r -s --argjson part 2  -f main.jq input-real

