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
	parse)
		set -x
		rm *.log
		./CvMain.py --action=parse --dir=/home/vishal/proj/tools/python/mail-reader/processed 1> test.log 2>&1
		;;
	parsepersist)
		set -x
		rm *.log
		./CvMain.py --action=parsepersist --dir=/home/vishal/proj/tools/python/mail-reader/processed 1> test.log 2>&1
		;;

	test)
		run_test
		;;

	*)
		echo "Invalid selection"
		;;
esac



