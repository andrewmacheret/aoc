[., .[$part * 2 - 1:]] | transpose | map(select(.[0] < .[1])) | length
