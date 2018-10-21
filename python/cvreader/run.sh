#!/usr/bin/ksh 

run_test()
{
	for f in $(find . -type f -name "*.py" -print)
	do
		echo '==============================='
		echo 'executing unittest >>>>> ' $f
		$f
		echo 'press any key ....'
		read 

	done
}

case $1 in
	run)
		set -x
		./CvMain.py --action=parse 1> test.log 2>&1
		;;

	test)
		run_test
		;;

	*)
		echo "Invalid selection"
		;;
esac



