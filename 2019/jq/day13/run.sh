#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 398      jq -R -r -s --argjson part 1 -f main.jq input.txt
test 19447    jq -R -r -s --argjson part 2 -f main.jq input.txt
