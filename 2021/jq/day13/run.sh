#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 17     jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 693    jq -R -r -s --argjson part 1  -f main.jq input-real

expected="
#####
#...#
#...#
#...#
#####"
test "$expected"      jq -R -r -s --argjson part 2  -f main.jq input-test-1

expected="
#..#..##..#....####.###...##..####.#..#
#..#.#..#.#.......#.#..#.#..#....#.#..#
#..#.#....#......#..#..#.#..#...#..#..#
#..#.#....#.....#...###..####..#...#..#
#..#.#..#.#....#....#.#..#..#.#....#..#
.##...##..####.####.#..#.#..#.####..##."
test "$expected"      jq -R -r -s --argjson part 2  -f main.jq input-real
