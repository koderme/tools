#!/bin/ksh

source ../common_ksh/base.ksh

#--------------------------------------------
# Setup
#--------------------------------------------
wp_setup()
{
	base_setup
	wp_download_dir=/var/tmp/wordpress
	wp_tar=latest.tar
	wp_tar_gz=latest.tar.gz
	apache_install_dir=/var/www/html
	wp_install_dir=$apache_install_dir
}

#--------------------------------------------
# wp post install
#--------------------------------------------
wp_ownership()
{
	chmod -R 755 wp-content
	chown -R www-data.www-data .
}

#--------------------------------------------
# Do action
#--------------------------------------------
wp_action()
{
	accept_user_response "Do you want to backup/restore (b:r)  " action

	if [ "$action" = "b" ] ; then
		wp_backup
	elif [ "$action" = "r" ] ; then
		wp_restore
	else
		err_exit "Invalid selection"
	fi

}

#--------------------------------------------
# wp_backup
#--------------------------------------------
wp_backup()
{
	prefix=wp
	backup_file=/var/tmp/$prefix.$now_datetime.tar.gz

	exec_cmd "cd /var/www/html"
	exec_cmd "tar -czvf $backup_file . 1> /dev/null"
	exec_cmd "openssl des3 < $backup_file > $backup_file.EN"

	log "create backup file $backup_file"
}

#--------------------------------------------
# wp_is_installed
#--------------------------------------------
wp_is_installed()
{
	[ -f $apache_install_dir/wp-config.php ] && return 0

	return 1
}

#--------------------------------------------
# wp_restore
#--------------------------------------------
wp_restore()
{
	continue_on_user_response "Are you running this with sudo? (y|N) : "
	accept_user_response "enter source file : " src_file
	[ ! -f $src_file ]  &&\
		err_exit "$src_file doesn't exist"

	wp_is_installed
	if [ $? -eq 0 ] ; then
		log "Previous installation exists..."
		continue_on_user_response "Do you want to backup this and proceed (y|n) ?"

		backup_dir=$apache_install_dir.$now_datetime
		exec_cmd "mv $apache_install_dir $backup_dir"
		log "wp backedup under $backup_dir"

	fi

	# Create empty dir for fresh installation
	exec_cmd "mkdir $apache_install_dir"
	wp_ownership


	# Restoring
	log "restoring from $src_file ..."

	# If its encrypted, decrypt it frst
	src_tar=/var/tmp/$now.tar.gz
	exec_cmd "openssl des3 -d < $src_file > $src_tar"
	
	exec_cmd "tar -xvzf $src_tar -C $apache_install_dir 1> /dev/null"

	exec_cmd "rm $src_tar"
}

#--------------------------------------------
# Main
#--------------------------------------------

wp_setup
wp_action

