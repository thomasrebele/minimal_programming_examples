#!/bin/bash

imgout="output/img/"

source common.sh

for i in $files; do
	dir=$(dirname $i)
	file=$(basename $i)
	mkdir -p $imgout/$dir
	echo $i

	png=$imgout/${i%.sh}.png

	[ ! -e $png -o $i -nt $png ] && (
		./run-example.sh $i


	)
done
