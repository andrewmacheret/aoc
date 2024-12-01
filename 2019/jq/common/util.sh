red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`
padding=16

test() {
  expected="$1"; shift
  actual="$( $* )"
  [[ "$expected" == "$actual" ]] && result="${green}PASS${reset}" || result="${red}FAIL${reset}"
  printf "$result ... expected = %-${padding}s actual = %-${padding}s\n" "$expected" "$actual"
}

test_multiline() {
  expected="$1"; shift
  actual="$( $* )"
  [[ "$expected" == "$actual" ]] && result="${green}PASS${reset}" || result="${red}FAIL${reset}"
  printf "$result ... expected =\n%s\nactual =\n%s\n\n" "$expected" "$actual"
}

cd "$( dirname "$0" )"
