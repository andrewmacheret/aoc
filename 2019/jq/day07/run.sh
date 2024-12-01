#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 43210  jq -R -r -s --argjson part 1 -f main.jq input-test-1.txt
test 54321  jq -R -r -s --argjson part 1 -f main.jq input-test-2.txt
test 65210  jq -R -r -s --argjson part 1 -f main.jq input-test-3.txt
test 24625  jq -R -r -s --argjson part 1 -f main.jq input.txt

test 139629729  jq -R -r -s --argjson part 2 -f main.jq input-test-4.txt
test 18216      jq -R -r -s --argjson part 2 -f main.jq input-test-5.txt
test 36497698   jq -R -r -s --argjson part 2 -f main.jq input.txt
