#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 0       jq -R -r -s --argjson part 1 -f <(cat ../common/util.jq main.jq) input-test-1
test 26      jq -R -r -s --argjson part 1 -f <(cat ../common/util.jq main.jq) input-test-2
test 488      jq -R -r -s --argjson part 1 -f <(cat ../common/util.jq main.jq) input-real

test 5353     jq -R -r -s --argjson part 2 -f <(cat ../common/util.jq main.jq) input-test-1
test 61229    jq -R -r -s --argjson part 2 -f <(cat ../common/util.jq main.jq) input-test-2
test 1040429  jq -R -r -s --argjson part 2 -f <(cat ../common/util.jq main.jq) input-real
