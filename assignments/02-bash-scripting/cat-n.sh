#!/bin/bash
FILE=$1

if [[ $# -eq 0 ]]; then
	echo "Usage: cat-n.sh FILE"
	exit 1
fi

if [[ ! -f $FILE ]]; then
	echo "$FILE is not a file"
	exit 1
fi

i=0
while read -r LINE; do
	i=$((i+1))
	echo $i "$LINE"
done < "$FILE"
