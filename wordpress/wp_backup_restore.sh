#!/usr/bin/ksh

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
	apache_install_dir=/var/www/html/
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
# wp post install
#--------------------------------------------
wp_post_install()
{
	cd $wp_install_dir

	accept_user_response "Enter project name (empty for home): " project_name

	if [ "$project_name" = "" ]; then

		continue_on_user_response "No project entered... Do you want to use $wp_install_dir? (y|N) : "

		# Check previous installation?
		[ -f wp-config.php ] && err_exit "Previous installation is present...please clean and retry" 

		exec_cmd "mv wordpress/* ."
		exec_cmd "rmdir wordpress"
	elif [ -d $project_name ]; then
		err_exit "$project_name already exists"
	else
		exec_cmd "mv wordpress $project_name"
		cd $project_name
	fi

	exec_cmd "cp wp-config-sample.php wp-config.php"

	wp_ownership
	exec_cmd "systemctl start apache2"

	log "Installation of wordpress is completed"
	log "Below steps are needed for complete installation"
	log " -- create db "
	log " -- create user and grant access to above db"
	log " -- edit $PWD/wp-config.php file with above credentials "
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

	cd /var/www/html
	exec_cmd "tar -czvf $backup_file ."

	log "create backup file $backup_file"
}

#--------------------------------------------
# wp_is_installed
#--------------------------------------------
wp_is_installed()
{
	cd $apache_install_dir

	[ -f wp-config.php ] && return 0

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
		continue_on_user_response "do you want to backup this and proceed (y|n) ?"

		backup_dir=$apache_install_dir.$now_datetime
		mv $apache_install_dir $backup_dir
		log "wp backedup under $backp_dir"
		mkdir $apache_install_dir
		wp_ownership
	fi

	cd $apache_install_dir
	exec_cmd "tar -xvfz $src_file ."
}

#--------------------------------------------
# Main
#--------------------------------------------

wp_setup
wp_action

