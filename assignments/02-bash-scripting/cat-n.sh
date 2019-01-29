#!/bin/bash
FILE=${1:-'sonnet-29.txt'}

if [[ $# -eq 0 ]]; then
	echo "Usage: cat-n.sh FILE"
	exit 1
fi

if [[ ! -f "$ARG" ]]; then
	echo "$ARG is not a file"
fi

i=0
while read -r LINE; do
	i=$((i+1))
	echo $i "$LINE"
done < "$FILE"
