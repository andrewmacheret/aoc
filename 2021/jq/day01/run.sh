#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 7    jq -s -f --arg part 1 main.jq input-test-1
test 1215 jq -s -f --arg part 1 main.jq input-real

test 5    jq -s -f --arg part 2 main.jq input-test-1
test 1150 jq -s -f --arg part 2 main.jq input-real
