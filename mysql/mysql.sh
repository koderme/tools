#---------------------------------------------
#---------------------------------------------
setup()
{
	#
	now=$(date '+%Y%m%d_%H%M%S')
	now_yyyymmdd=$(date '+%Y%m%d')
	logfile=/var/tmp/$now.log
}

#---------------------------------------------
#---------------------------------------------
err_exit()
{
	echo $*
	exit 1
}

#---------------------------------------------
#---------------------------------------------
exec_cmd()
{
	cmd=$1
	eval $cmd  >> $logfile
	if [ $? -eq 0 ] ; then
		echo "success : [$cmd]"
	else
		echo "fail : [$cmd]"
		err_exit ""
	fi
}

#---------------------------------------------
#---------------------------------------------
verify()
{
	for var in $*
	do
		unset v
		cmd="v=\$$var"
		eval $cmd
		[ "${v}z" = "z" ] &&
			err_exit "$var not specified"
	done
}

#---------------------------------------------
#---------------------------------------------
read_and_verify()
{
	echo -n "enter: $1"
	read $1	

	for var in $1
	do
		cmd="v=\$$var"
		echo [$cmd]
		eval $cmd
		[ ${v:zzz} = "zzz" ] &&
			err_exit "$var not set"
	done
}



#---------------------------------------------
#---------------------------------------------
mysql_dbdump()
{
	#echo "eg: 192.168.1.36 kesar2_restore gharat" 
	db_dump_file=/var/tmp/$USER.$db_name.$now_yyyymmdd.sql
	exec_cmd "mysqldump --host $db_host --user $db_user -p $db_name > $db_dump_file"
	echo "dump successful : $db_dump_file"
}

#---------------------------------------------
#---------------------------------------------
mysql_restore()
{
	exec_cmd "mysql --host $db_host --user $db_user -p $db_name < $restore_file"
	echo "restored $db_restore_file"
}

#---------------------------------------------
#---------------------------------------------
mysql_create_schema()
{
	cr_schema_sql=$(tempfile)
	echo "create database $db_name;" > $cr_schema_sql

	exec_cmd "mysql --host $db_host --user $db_user --password  < $cr_schema_sql"
	echo "created schema $db_name "
}

#---------------------------------------------
#---------------------------------------------
recv_user_response()
{
	echo -n "do you want to continue? " 
	read response
	[ ${response:zz} != "y" ] && exit
}

#---------------------------------------------
#---------------------------------------------
read_args()
{
	while getopts "a:h:d:u:f:" opt
	do
		case $opt in
			a)
			action=$OPTARG ;;
			h)
			db_host=$OPTARG ;;
			d)
			db_name=$OPTARG ;;
			u)
			db_user=$OPTARG ;;
			
			f)
			restore_file=$OPTARG ;;
			\?)
			err_exit "Invalid arg" ;;
		esac
	done

	verify action
}

#---------------------------------------------
#---------------------------------------------
do_action()
{
	if [ "${action}" = "backup" ] ; then
		verify db_host db_name db_user
		mysql_dbdump
	fi

	if [ "${action}" = "restore" ] ; then
		verify db_host db_name db_user restore_file
		mysql_create_schema
		mysql_restore
	fi
}

#---------------------------------------------
#---------------------------------------------
show_usage()
{
cat<<EOF
	$0 option arg
	  -a  action [backup restore]
	  -h  host
	  -d  database name/schema name
	  -u  user
	  -f  restore file path

	e.g.

	./mysql.sh  -a backup -h 192.168.1.33 -d kesar -u gharat

	./mysql.sh  -a restore -h 192.168.1.36 -d kesar_restore -u admin -f /var/tmp/gharat.kesar.20180719.sql

EOF

}


#-----------------------------
# Main
#-----------------------------
setup
read_args $*

do_action
[ -f $logfile ] && echo "see log $logfile"
