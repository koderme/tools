#!/bin/ksh

source ../common_ksh/base.ksh


#---------------------------------------------
#---------------------------------------------
mysql_dbdump()
{
	db_dump_file=/var/tmp/$USER.$db_name.$now_yyyymmdd.sql
	exec_cmd "mysqldump --host $db_host --user $db_user -p $db_name > $db_dump_file"
	echo "compressing the file ... "
	exec_cmd "gzip $db_dump_file"
	echo "encrpting the file ... "
	exec_cmd "openssl des3 < $db_dump_file.gz > $db_dump_file.gz.EN"
	exec_cmd "rm $db_dump_file.gz"
	echo ""
	echo "dump successful : $db_dump_file.gz.EN"
}

#---------------------------------------------
#---------------------------------------------
mysql_restore()
{
	tmp_file=/var/tmp/$now.sql
	tmp_file_gz=$tmp_file.gz

	echo "decrypting file ... "
	exec_cmd "openssl des3 -d < $restore_file > $tmp_file_gz "

	echo "unzipping file ... "
	exec_cmd "gunzip $tmp_file_gz"

	exec_cmd "mysql --host $db_host --user $db_user -p $db_name < $tmp_file"
	exec_cmd "rm $tmp_file"
	echo "restored db from $db_restore_file"
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

	$0  -a backup -h 192.168.1.36 -d ksp_db -u ksp_adm

	$0  -a restore -h 192.168.1.36 -d ksp_db -u ksp_adm -f /var/tmp/gharat.kesar.20180719.sql

EOF

}


#-----------------------------
# Main
#-----------------------------
base_setup
read_args $*

do_action
[ -f $logfile ] && echo "see log $logfile"
