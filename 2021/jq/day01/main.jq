[[., .[$part * 2 - 1:]] | transpose[] | select(.[0] < .[1])] | length