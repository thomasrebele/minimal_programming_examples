#!/bin/bash

source common.sh

desc=$(grep '<!-- description' $1 | sed 's/.*description: \(.*\) -->/web: \1/')

code=$(awk '
	BEGIN { first=1; out=0; } 
	/<!-- start/ { 
		out=1; 
		if(first==1) {first=0} 
		else {print("...")};
		next
	} 
	/<!-- end/ {out=0} 
	out==1 { print $0}' $1 | html_encode | sed 's/\t/\&#9;/g' | sed 's/$/<br\/>/g' | tr -d '\n')

img="<img src=\"${1%.html}.png\">"

if [ "$no_hierarchy" == "1" ]; then
	img=${img//\//-}
fi

desc_lines=$(echo "$desc" | wc -l)
if [ "$desc_lines" != "1" ]; then
	echo "one line of description needed, got $desc_lines in $1" 1>&2
elif [ "$code" == "" ]; then
	echo "start/end tag missing in $1" 1>&2
else
	echo "$img"$'\t'"$desc"$'\t'"$code"
fi
