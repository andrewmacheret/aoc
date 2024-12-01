#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 13787043  jq -R -r -s --argjson part 1  -f main.jq input.txt
test 3892695   jq -R -r -s --argjson part 2  -f main.jq input.txt
