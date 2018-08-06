#!/bin/ksh

source ../common_ksh/base.ksh

#--------------------------------------------
# Setup
#--------------------------------------------
wp_setup()
{
	base_setup
	wp_download_dir=../../backup/wp_base/
	wp_tar_gz=latest.tar.gz
	apache_install_dir=/var/www/html/
	wp_install_dir=$apache_install_dir
}

#--------------------------------------------
# download wp tar
#--------------------------------------------
wp_download()
{
	continue_on_user_response "Are you running this with sudo? (y|N) : "

	if [ ! -f $wp_download_dir/$wp_tar_gz ] ; then
		exec_cmd "mkdir -p $wp_download_dir"
		cd $wp_download_dir
		exec_cmd "wget https://wordpress.org/$wp_tar_gz"
	else
		log "$wp_download_dir/$wp_tar_gz is already present"
		continue_on_user_response "Do you want to use this? (y|N) : "
	fi
}

#--------------------------------------------
# wp install
#--------------------------------------------
wp_install()
{
	exec_cmd "tar -xvzf $wp_download_dir/$wp_tar_gz -C $wp_install_dir"
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

	chmod -R 755 wp-content
	chown -R www-data.www-data .
	exec_cmd "systemctl start apache2"

	log "Installation of wordpress is completed"
	log "Below steps are needed for complete installation"
	log " -- create db "
	log " -- create user and grant access to above db"
	log " -- edit $PWD/wp-config.php file with above credentials "
}

#--------------------------------------------
# Main
#--------------------------------------------

wp_setup
wp_download
wp_install
wp_post_install
log 

