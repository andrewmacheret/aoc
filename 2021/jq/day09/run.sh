#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 15       jq -R -r -s --argjson part 1 -f <(cat ../common/util.jq main.jq) input-test-1
test 554      jq -R -r -s --argjson part 1 -f <(cat ../common/util.jq main.jq) input-real

test 1134     jq -R -r -s --argjson part 2 -f <(cat ../common/util.jq main.jq) input-test-1
test 1017792  jq -R -r -s --argjson part 2 -f <(cat ../common/util.jq main.jq) input-real
