#!/bin/bash

FILE=$1
NUMLINES=$2
i=0

if [[ $# -eq 0 ]]; then
	echo "Usage: head.sh FILE NUMLINES"
	exit 1
fi

if [[ ! -f $FILE ]]; then 
	echo "$FILE is not a file"
	exit 1
fi

if [[ $NUMLINES -eq 0 ]]; then
	NUMLINES=3
fi

while read -r LINE; do
	i=$((i+1))
	echo $i "$LINE"
	if [[ $i -eq $NUMLINES ]]; then
		break
	fi
done < "$FILE"
