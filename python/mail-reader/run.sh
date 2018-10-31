#!/usr/bin/ksh

case $1 in
	download)
		./Main.py --action=download --dir=downloads
		;;

	parse)
		./Main.py --action=parse --dir=downloads
		;;

	*)
		echo "Invalid selection"
		;;
esac
