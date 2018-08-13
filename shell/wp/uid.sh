#!/bin/ksh

source ../common_ksh/base.ksh


#---------------------------------------------
# Set useful var
#---------------------------------------------
uid_setup()
{
	module_list="wp db"
	role_list="adm usr"

	application_list="hkr ksp"
}

#---------------------------------------------
# Generates uid
# @arg application
# @arg Role
#---------------------------------------------
generate_uid()
{
	application=$1
	role=$2

	validate_in_list $application "$application_list"
	validate_in_list $role "$role_list"

	echo ${application}_${role}
}

#---------------------------------------------
# Generates uid
# @arg Module
# @arg Portal type
# @arg Role
# @arg application
#---------------------------------------------
generate_uid_complex()
{
	module=$1
	role=$3
	application=$4

	validate_in_list $module "$module_list"
	validate_in_list $role "$role_list"
	validate_in_list $application "$application_list"

	echo ${module}_${role}_${application}
}

#---------------------------------------------
# Generates dbname
# @arg Portal type
# @arg application
#---------------------------------------------
generate_dbname()
{
	application=$1

	validate_in_list $application "$application_list"

	echo ${application}_db
}

#---------------------------------------------
# Main
#---------------------------------------------Q
uid_setup

# ------------------------
app=hkr
echo "------ for $portal_type -------"

# uid
generate_uid $app adm
generate_uid $app usr

# dbname
generate_dbname $app 


# ------------------------
app=hkr
echo "------ for $portal_type -------"

# uid
generate_uid $app adm
generate_uid $app usr

# dbname
generate_dbname $app 


