#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 4512   jq -R -r -s --argjson part 1 -f main.jq input-test-1
test 21607  jq -R -r -s --argjson part 1 -f main.jq input-real

test 1924   jq -R -r -s --argjson part 2 -f main.jq input-test-1
test 19012  jq -R -r -s --argjson part 2 -f main.jq input-real
