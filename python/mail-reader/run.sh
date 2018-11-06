#!/usr/bin/ksh

case $1 in
	download)
		./Main.py --action=download --dir=downloads
		;;

	converttotext)
		./Main.py --action=converttotext --dir=sample_cv
		;;

	*)
		echo "Invalid selection"
		;;
esac
