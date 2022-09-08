#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 26397       jq -R -r -s --argjson part 0 -f <(cat ../common/util.jq main.jq) input-test-1
test 345441      jq -R -r -s --argjson part 0 -f <(cat ../common/util.jq main.jq) input-real

test 288957      jq -R -r -s --argjson part 1 -f <(cat ../common/util.jq main.jq) input-test-1
test 3235371166  jq -R -r -s --argjson part 1 -f <(cat ../common/util.jq main.jq) input-real
