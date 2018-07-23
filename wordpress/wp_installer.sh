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
# download wp tar
#--------------------------------------------
wp_download()
{
	if [ ! -f $wp_download_dir/$wp_tar ] ; then
		mkdir -p $wp_download_dir 2> /dev/null
		cd $wp_download_dir
		exec_cmd "wget https://wordpress.org/$wp_tar_gz"
		exec_cmd "gunzip  $wp_tar_gz"
	else
		log "$wp_tar is already present"
		continue_on_user_response "Do you want to use this? "
	fi
}

#--------------------------------------------
# wp install
#--------------------------------------------
wp_install()
{
	cd $wp_install_dir

	exec_cmd "tar -xvf $wp_download_dir/$wp_tar "
}

#--------------------------------------------
# wp post install
#--------------------------------------------
wp_post_install()
{
	cd $wp_install_dir

	accept_user_response "Enter project name : " project_name

	if [ -d $project_name ]; then
		err_exit "$project_name already exists"
	fi

	mv wordpress $project_name

	cd $project_name

	exec_cmd "cp wp-config-sample.php wp-config.php"

	chmod -R 755 wp-content
	chown -R www-data.www-data .
	exec_cmd "systemctl start apache2"

	log "Installation of wordpress is completed"
	log "Edit $PWD/wp-config.php file"
}

#--------------------------------------------
# Main
#--------------------------------------------

wp_setup
wp_download
wp_install
wp_post_install
log 

