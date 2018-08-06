#!/bin/ksh

#---------------------------------------------
# Set useful var
#---------------------------------------------
base_setup()
{
	#
	now=$(date '+%Y%m%d_%H%M%S')
	now_yyyymmdd=$(date '+%Y%m%d')
	now_date=$(date '+%Y%m%d')
	now_datetime=$(date '+%Y%m%d_%H%M%S')
	logfile=/var/tmp/$now.log
}

#---------------------------------------------
# exit with error
# @arg    Message to be displayed
#---------------------------------------------
err_exit()
{
	echo $*
	exit 1
}

#---------------------------------------------
# @arg    Message to be logger
#---------------------------------------------
log()
{
	echo $* | tee -a $logfile
}


#---------------------------------------------
# Execute the specified command
# @arg Command
#---------------------------------------------
exec_cmd()
{
	cmd=$1
	eval $cmd  1> $logfile 2>&1
	if [ $? -eq 0 ] ; then
		echo " success : [$cmd]"
	else
		echo " fail : [$cmd]"
		err_exit ""
	fi
}

#---------------------------------------------
# Verify that specified variables have been set
# @arg list of arguments
#---------------------------------------------
verify()
{
	for var in $*
	do
		unset v
		cmd="v=\$$var"
		eval $cmd
		if [ "${v}z" = "z" ] ; then
			err_exit "$var not specified"
			show_usage
		fi
	done
}

#---------------------------------------------
# Read the variables from stdin
# @arg List of arguments to be read
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
# Prompts for user response to continue
# @arg Prompt to be displayed
#---------------------------------------------
accept_user_response()
{
	prompt=$1
	echo -n $prompt
	read response
	eval "$2=$response"
}

#---------------------------------------------
# Prompts for user response to continue
# @arg Prompt to be displayed
#---------------------------------------------
continue_on_user_response()
{
	prompt=$*
	echo -n $prompt
	read response
	[ "${response:zz}" != "y" -a "${response:zz}" != "Y" ] && exit
}

#---------------------------------------------
# Checks if its in list
# @arg value
# @arg list
#---------------------------------------------
validate_in_list()
{
	value=$1
	list=$2

	for v in $list
	do
		[ "$value" = "$v" ] && return
	done

	err_exit "Invalid $value not in [$list]"
}

