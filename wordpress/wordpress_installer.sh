#!/bin/bash

wp_download_dir=/var/tmp/wordpress
wp_tar=latest.tar
wp_tar_gz=latest.tar.gz
apache_install_dir=/var/www/html/

if [ ! -f $wp_download_dir/$wp_tar ] ; then
	mkdir -p $wp_download_dir
	cd $wp_download_dir
	wget https://wordpress.org/$wp_tar_gz
	gunzip  $wp_tar_gz
else
	echo "$wp_tar is already present" 
	echo "press any key to continue..."
	read junk
fi

echo "extracting ..."
cd $apache_install_dir
tar -xvf $wp_download_dir/$wp_tar 1> /dev/null 2>&1

echo -n "project name :" 
read  project_name

if [ -d $project_name ]; then
	echo "$project_name already exists"
	exit
fi

mv wordpress $project_name
cd $project_name

echo "Copying wordpress ..."
cp  wp-config-sample.php wp-config.php
chmod -R 755 wp-content
chown -R www-data.www-data .
systemctl start apache2

echo "Installation of wordpress is completed"
echo "Edit wp-config.php file"
