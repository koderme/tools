#!/usr/bin/ksh

for f in $(find . -type f)
do
	mv $f .
done
